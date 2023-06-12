const userForm = document.querySelector('#userForm');
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
  const password = userForm['password'].value;
  const email = userForm['email'].value;

  if (!editing) {
    const response = await fetch('/api/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username,
        password,
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
        password,
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

function renderUser(users) {
  const userList = document.querySelector('#userList');
  console.log(userList);
  userList.innerHTML = '';
  users.forEach((user) => {
    const userItem = document.createElement('li');
    userItem.classList = 'list-group-item list-group-item-dark my-2';
    userItem.innerHTML = `
      <header class="d-flex justify-content-between align-items-center">
        <h3>${user.username}</h3>
        <div>  
          <button class="btn-delete btn btn-danger btn-sm">Delete</button>
          <button class="btn-edit btn btn-secondary btn-sm">Edit</button>
        </div>
      </header>
      <p>${user.email}</p>
      <p class="text-truncate">${user.password}</p>
    `;

    const btnDelete = userItem.querySelector('.btn-delete');
    btnDelete.addEventListener('click', async () => {
      const response = await fetch(`/api/users/${user.id}`, {
        method: 'DELETE',
      });
      const data = await response.json();
      users = users.filter((u) => u.id !== data.id);
      renderUser(users);
    });

    const btnEdit = userItem.querySelector('.btn-edit');
    btnEdit.addEventListener('click', async () => {
      const response = await fetch(`/api/users/${user.id}`);
      const data = await response.json();

      userForm['username'].value = data.username;
      userForm['email'].value = data.email;
      editing = true;
      userId = data.id;
    });

    userList.appendChild(userItem);
  });
}