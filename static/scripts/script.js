document.addEventListener("DOMContentLoaded", function() {
  const dropdowns = document.querySelectorAll('.status-dropdown');

  dropdowns.forEach(dropdown => {
    dropdown.addEventListener('change', function() {
      const clientId = dropdown.getAttribute('data-client-id');
      const status = dropdown.value;

      updateClientStatus(clientId, status);
    });
  });

  function updateClientStatus(clientId, status) {
    fetch(`/change_status/?client_id=${clientId}&status=${status}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      },
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        // Обновляем статус на странице
        const statusDropdown = document.querySelector(`.status-dropdown[data-client-id="${clientId}"]`);
        statusDropdown.value = status;
      } else {
        console.error('Ошибка при обновлении статуса');
      }
    })
    .catch(error => {
      console.error('Ошибка:', error);
    });
  }

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
});
