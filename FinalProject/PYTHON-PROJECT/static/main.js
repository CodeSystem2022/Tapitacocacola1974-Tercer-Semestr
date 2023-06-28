const userForm = document.querySelector('#userForm');//comenzamos seleccionando user form desde el DOM  donde crearemos las tarjetas con los datos traidos desde el back
let users = [];
let editing = false;
let userId = null;

window.addEventListener('DOMContentLoaded', async () => { // cuando el documento se cargue pedira el codigo al backend
  const response = await fetch('/api/users');
  const data = await response.json();
  console.log(data);
  users = data;
  renderUser(users);
});

userForm.addEventListener('submit', async (e) => {//aqui con el boton submit podemos enviar los datos del formulario
  e.preventDefault();

  const username = userForm['username'].value;
  const direccion = userForm['direccion'].value;
  const email = userForm['email'].value;

  if (!editing) {//se hace uso del metodo post para enviar datos al servidor
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
    const response = await fetch(`/api/users/${userId}`, {//en este caso se hace uso del metodo put para hacer updating de datos
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
    users = users.map(user => user.id === updateUser.id ? updateUser : user);//se renderiza los datos guardados en render user
    renderUser(users);
    editing = false;
    userId = null;
  }

  renderUser(users);
  userForm.reset();
});

function renderUser(users) {//en esta funcion se ira creando en el DOM los datos correspondientes renderizando la informacion
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

    const btnDelete = userItem.querySelector('.btn-delete');//se crea la funcion de boton delete
    btnDelete.addEventListener('click', async () => {
      const response = await fetch(`/api/users/${user.id}`, {
        method: 'DELETE',
      });
      const data = await response.json();
      users = users.filter((u) => u.id !== data.id);
      renderUser(users);
    });

    const btnEdit = userItem.querySelector('.btn-edit');//se crean las funciones de envento en este caso edit
    btnEdit.addEventListener('click', async () => {
      const response = await fetch(`/api/users/${user.id}`);
      const data = await response.json();

      userForm['username'].value = data.username;
      userForm['email'].value = data.email;
      userForm['direccion'].value = data.direccion
      editing = true;
      userId = data.id;
    });

    const dropdownToggle = userItem.querySelector('.dropdown-toggle');//hicimos uso de boostrap para este boton desplegable
    const dropdownMenu = userItem.querySelector('.dropdown-menu');
    dropdownToggle.addEventListener('click', () => {
      dropdownMenu.classList.toggle('show');
    });

    userList.appendChild(userItem);
  });
}

const divElement = document.getElementById('desple');
divElement.style.display = 'none'
const hideButton = document.getElementById('botondesple');

// simplemente se crea una funcion para desplegar no la informacion obtenida desde el backend
hideButton.addEventListener('click', function() {
  if(divElement.style.display === 'none'){
    divElement.style.display = 'block'
  }else{
    divElement.style.display = 'none'
  }
  
});
