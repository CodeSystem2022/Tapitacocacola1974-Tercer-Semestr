const userForm = document.querySelector('#userForm'); //iniciamos manipulando el dom 
let users = [];
let editing = false;
let userId = null;

window.addEventListener('DOMContentLoaded', async () => {
  const response = await fetch('/api/users');
  const data = await response.json();
  console.log(data);
  users = data;
  renderUser(users);
});

userForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const username = userForm['username'].value;
  const direccion = userForm['direccion'].value;
  const email = userForm['email'].value;

  if (!editing) {
    const response = await fetch('/api/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username,
        direccion,
        email,
      }),
    });

    const data = await response.json();
    users.unshift(data);
  } else {
    const response = await fetch(`/api/users/${userId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username,
        direccion,
        email,
      }),
    });

    const updateUser = await response.json();
    users = users.map(user => user.id === updateUser.id ? updateUser : user);
    renderUser(users);
    editing = false;
    userId = null;
  }

  renderUser(users);
  userForm.reset();
});

function renderUser(users) { //con esta funcion lo que hacemos es renderizar la informacion obtenida desde el backend o recibida desde el front end
  const userList = document.querySelector('#userList');
  console.log(userList);
  userList.innerHTML = '';
  users.forEach((user) => {
    const userItem = document.createElement('li');
    userItem.classList = 'list-group-item list-group-item-dark my-2';
    userItem.innerHTML = `
      <header class="d-flex justify-content-between align-items-center">
        <h3>${user.username}</h3>
        <div class="dropdown">
          <button class="btn btn-secondary bg-primary btn-sm dropdown-toggle" type="button" id="dropdownMenuButton${user.id}" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Acciones
          </button>
          <div class="dropdown-menu bg-primary" aria-labelledby="dropdownMenuButton${user.id}">
            <button class="dropdown-item btn-delete">Eliminar</button>
            <button class="dropdown-item btn-edit">Editar</button>
          </div>
        </div>
      </header>
      <p>${user.email}</p>
      <p>${user.direccion}</p>
    `;

    const btnDelete = userItem.querySelector('.btn-delete'); //en este boton delete hemos creado una funcion que al clickear eliminael dato deseado
    btnDelete.addEventListener('click', async () => {
      const response = await fetch(`/api/users/${user.id}`, {
        method: 'DELETE',
      });
      const data = await response.json();
      users = users.filter((u) => u.id !== data.id);
      renderUser(users);
    });

    const btnEdit = userItem.querySelector('.btn-edit'); // hemos creado una funcion en la cual el boton edit nos permite editar lo deseado
    btnEdit.addEventListener('click', async () => {
      const response = await fetch(`/api/users/${user.id}`);
      const data = await response.json();

      userForm['username'].value = data.username;
      userForm['email'].value = data.email;
      userForm['direccion'].value = data.direccion
      editing = true;
      userId = data.id;
    });

    const dropdownToggle = userItem.querySelector('.dropdown-toggle');
    const dropdownMenu = userItem.querySelector('.dropdown-menu');
    dropdownToggle.addEventListener('click', () => {
      dropdownMenu.classList.toggle('show');
    });

    userList.appendChild(userItem);
  });
}