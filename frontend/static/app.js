const BASE_URL = 'http://127.0.0.1:5000';

// Завантаження компонентів у випадаючий список
async function loadComponents(category, elementId) {
    try {
        const response = await fetch(`${BASE_URL}/components?category=${category}`);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        const select = document.getElementById(elementId);
        select.innerHTML = ''; // Очищуємо список перед додаванням

        // Додаємо опцію "Виберіть компонент"
        const defaultOption = document.createElement('option');
        defaultOption.value = '';
        defaultOption.textContent = 'Виберіть компонент';
        select.appendChild(defaultOption);

        // Додаємо компоненти до списку
        data.forEach(item => {
            const option = document.createElement('option');
            option.value = item.name;
            option.textContent = item.name;
            option.dataset.power = item.power || 0; // Додаткові дані
            select.appendChild(option);
        });
    } catch (error) {
        console.error(`Помилка завантаження компонентів (${category}):`, error);
    }
}

// Оновлення енергоспоживання
function updateConsumption() {
    const powerElements = ['cpu', 'gpu', 'ram', 'ssd', 'motherboard'];
    let totalPower = 0;

    powerElements.forEach(id => {
        const element = document.getElementById(id);
        if (element && element.selectedIndex >= 0) {
            const power = parseInt(element.options[element.selectedIndex]?.dataset.power || '0', 10);
            totalPower += power;
        }
    });

    // Оновлення значення на сторінці
    document.getElementById('powerConsumption').textContent = totalPower;
}

// Перевірка сумісності
async function checkCompatibility() {
    try {
        const components = getSelectedComponents(); // Отримуємо вибрані компоненти
        const response = await fetch(`${BASE_URL}/compatibility`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ components })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const result = await response.json();
        const output = document.getElementById('compatibilityResult');

        if (result.compatible) {
            // Якщо всі компоненти сумісні
            output.textContent = result.message || 'Усі компоненти сумісні!';
            output.style.color = 'green';
        } else if (result.issues && Array.isArray(result.issues)) {
            // Якщо є помилки
            output.textContent = `Проблеми: ${result.issues.join(', ')}`;
            output.style.color = 'red';
        } else {
            // Якщо перевірка завершилася невдало
            output.textContent = 'Не вдалося перевірити сумісність.';
            output.style.color = 'orange';
        }        
    } catch (error) {
        console.error('Error checking compatibility:', error);
        const output = document.getElementById('compatibilityResult');
        output.textContent = 'Під час перевірки сумісності сталася помилка. Спробуйте пізніше.';
        output.style.color = 'red';
    } finally {
        console.log('Compatibility check completed.');
    }
}

function getSelectedComponents() {
    const components = {
        "CPU": document.getElementById('cpu').value || "",
        "GPU": document.getElementById('gpu').value || "",
        "RAM": document.getElementById('ram').value || "",
        "SSD": document.getElementById('ssd').value || "",
        "Motherboard": document.getElementById('motherboard').value || "",
        "Power Supply": document.getElementById('psu').value || ""
    };
    console.log("Selected components for compatibility check:", components);
    return components;
}

function getSelectedComponent(elementId) {
    const element = document.getElementById(elementId);
    const name = element.options[element.selectedIndex]?.text || '';
    const power = parseInt(element.options[element.selectedIndex]?.dataset.power || '0', 10);
    const socket = element.options[element.selectedIndex]?.dataset.socket || '';
    const type = element.options[element.selectedIndex]?.dataset.type || '';
    return { name, power, socket, type };
}

// Чат із AI
async function sendMessage() {
    const input = document.getElementById('chat-input');
    const userMessage = input.value.trim();

    if (!userMessage) return;

    const chatMessages = document.getElementById('chat-messages');

    // Додаємо повідомлення користувача
    const userMessageElement = document.createElement('div');
    userMessageElement.textContent = `Ви: ${userMessage}`;
    userMessageElement.classList.add('user-message');
    chatMessages.appendChild(userMessageElement);

    input.value = ''; // Очищення поля вводу

    try {
        const response = await fetch(`${BASE_URL}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userMessage })
        });

        const data = await response.json();
        const reply = data.reply;

        // Додаємо відповідь AI
        const botMessageElement = document.createElement('div');
        botMessageElement.classList.add('bot-message');

        // Форматування списків (нові рядки або маркери 1., 2., ...)
        const formattedReply = reply
            .split(/\n/) // Розділення за новими рядками
            .map(line => {
                const listItem = document.createElement('div');
                listItem.textContent = line.trim();
                return listItem;
            });

        // Додаємо кожен рядок як окремий елемент
        formattedReply.forEach(item => botMessageElement.appendChild(item));

        chatMessages.appendChild(botMessageElement);

        // Автопрокрутка до останнього повідомлення
        chatMessages.scrollTop = chatMessages.scrollHeight;
    } catch (error) {
        console.error('Помилка відправлення повідомлення:', error);
    }
}

function applyFilters() {
    const manufacturer = document.getElementById('cpu-manufacturer').value;
    const socket = document.getElementById('cpu-socket').value;

    fetch(`${BASE_URL}/components?category=CPU`)
        .then(response => response.json())
        .then(data => {
            const filtered = data.filter(cpu => {
                return (
                    (manufacturer === '' || cpu.manufacturer === manufacturer) &&
                    (socket === '' || cpu.socket === socket)
                );
            });

            updateComponentList('cpu', filtered);
        });
}

function applyGPUFilters() {
    const manufacturer = document.getElementById('gpu-manufacturer').value;
    const memory = document.getElementById('gpu-memory').value;

    fetch(`${BASE_URL}/components?category=GPU`)
        .then(response => response.json())
        .then(data => {
            const filtered = data.filter(gpu => {
                return (
                    (manufacturer === '' || gpu.manufacturer === manufacturer) &&
                    (memory === '' || gpu.memory === memory)
                );
            });

            updateComponentList('gpu', filtered);
        });
}
document.getElementById('gpu-manufacturer').addEventListener('change', applyGPUFilters);
document.getElementById('gpu-memory').addEventListener('change', applyGPUFilters);

function applyRAMFilters() {
    const type = document.getElementById('ram-type').value;
    const frequency = document.getElementById('ram-frequency').value;

    fetch(`${BASE_URL}/components?category=RAM`)
        .then(response => response.json())
        .then(data => {
            const filtered = data.filter(ram => {
                return (
                    (type === '' || ram.type === type) &&
                    (frequency === '' || ram.frequency === frequency)
                );
            });

            updateComponentList('ram', filtered);
        });
}
document.getElementById('ram-type').addEventListener('change', applyRAMFilters);
document.getElementById('ram-frequency').addEventListener('change', applyRAMFilters);

function applyMotherboardFilters() {
    const socket = document.getElementById('motherboard-socket').value;
    const memoryType = document.getElementById('motherboard-memory-type').value;

    fetch(`${BASE_URL}/components?category=Motherboard`)
        .then(response => response.json())
        .then(data => {
            const filtered = data.filter(motherboard => {
                return (
                    (socket === '' || motherboard.socket === socket) &&
                    (memoryType === '' || motherboard.memory_type === memoryType)
                );
            });

            updateComponentList('motherboard', filtered);
        });
}
document.getElementById('motherboard-socket').addEventListener('change', applyMotherboardFilters);
document.getElementById('motherboard-memory-type').addEventListener('change', applyMotherboardFilters);

function applySSDFilters() {
    const formFactor = document.getElementById('ssd-form-factor').value;
    const capacity = document.getElementById('ssd-capacity').value;

    fetch(`${BASE_URL}/components?category=SSD`)
        .then(response => response.json())
        .then(data => {
            const filtered = data.filter(ssd => {
                return (
                    (formFactor === '' || ssd.form_factor === formFactor) &&
                    (capacity === '' || ssd.capacity === capacity)
                );
            });

            updateComponentList('ssd', filtered);
        });
}
document.getElementById('ssd-form-factor').addEventListener('change', applySSDFilters);
document.getElementById('ssd-capacity').addEventListener('change', applySSDFilters);

function applyPSUFilters() {
    const power = document.getElementById('psu-power').value;

    fetch(`${BASE_URL}/components?category=Power%20Supply`)
        .then(response => response.json())
        .then(data => {
            const filtered = data.filter(psu => {
                return power === '' || psu.power.toString() === power;
            });

            updateComponentList('psu', filtered);
        });
}
document.getElementById('psu-power').addEventListener('change', applyPSUFilters);

function updateComponentList(elementId, components) {
    const select = document.getElementById(elementId);
    select.innerHTML = '<option value="">Виберіть компонент</option>';
    components.forEach(component => {
        const option = document.createElement('option');
        option.value = component.name;
        option.textContent = component.name;
        select.appendChild(option);
    });
}

document.getElementById('cpu-manufacturer').addEventListener('change', applyFilters);
document.getElementById('cpu-socket').addEventListener('change', applyFilters);

// Завантаження компонентів при завантаженні сторінки
document.addEventListener('DOMContentLoaded', () => {
    loadComponents('CPU', 'cpu');
    loadComponents('GPU', 'gpu');
    loadComponents('RAM', 'ram');
    loadComponents('SSD', 'ssd');
    loadComponents('Motherboard', 'motherboard');
    loadComponents('Power Supply', 'psu');

    loadReadyBuilds(); 
});

// Завантаження готових збірок
async function loadReadyBuilds() {
    try {
        const response = await fetch(`${BASE_URL}/builds`);
        if (!response.ok) {
            console.error(`Помилка HTTP: ${response.status}`);
            return;
        }
        const builds = await response.json();

        const buildsContainer = document.getElementById('ready-builds');
        buildsContainer.innerHTML = ''; // Очищаємо блок перед додаванням

        builds.forEach(build => {
            const buildElement = document.createElement('div');
            buildElement.classList.add('build-item');
            buildElement.innerHTML = `
                <h4>${build.name} (${build.purpose})</h4>
                <ul>
                    <li><strong>CPU:</strong> ${build.components.CPU}</li>
                    <li><strong>GPU:</strong> ${build.components.GPU}</li>
                    <li><strong>RAM:</strong> ${build.components.RAM}</li>
                    <li><strong>Motherboard:</strong> ${build.components.Motherboard}</li>
                    <li><strong>SSD:</strong> ${build.components.SSD}</li>
                    <li><strong>Power Supply:</strong> ${build.components["Power Supply"]}</li>
                </ul>
                <p><strong>Сумарне енергоспоживання:</strong> ${build.total_power} Вт</p>
            `;
            buildsContainer.appendChild(buildElement);
        });
    } catch (error) {
        console.error('Помилка завантаження готових збірок:', error);
    }
}

let savedBuilds = []; // Масив для збережених збірок

function saveBuild(name, components, totalPower) {
    const build = {
        id: Date.now(),
        name,
        components,
        totalPower
    };

    savedBuilds.push(build);
    localStorage.setItem('savedBuilds', JSON.stringify(savedBuilds)); // Зберігаємо в localStorage
    updateSavedBuildsUI();
}

// Завантаження збірок з localStorage при старті
window.onload = function () {
    const storedBuilds = JSON.parse(localStorage.getItem('savedBuilds'));
    if (storedBuilds) {
        savedBuilds = storedBuilds;
        updateSavedBuildsUI();
    }
};

// Оновлення списку збірок
// Оновлення списку збірок
function updateSavedBuildsUI() {
    const list = document.getElementById('saved-builds-list');
    list.innerHTML = '';

    savedBuilds.forEach(build => {
        const li = document.createElement('li');

        // Створюємо текстову частину для назви збірки
        const buildText = document.createElement('span');
        buildText.textContent = `${build.name} – Енергоспоживання: ${build.totalPower} Вт`;
        buildText.classList.add('build-text'); // Для стилів, якщо потрібно
        buildText.addEventListener('click', () => showBuildDetails(build.id)); // Відображення деталей
        li.appendChild(buildText);

        // Додаємо кнопку видалення
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Видалити';
        deleteButton.classList.add('delete-button'); // Додаємо клас для стилізації
        deleteButton.addEventListener('click', (e) => {
            e.stopPropagation(); // Запобігаємо виклику showBuildDetails
            deleteBuild(build.id);
        });
        li.appendChild(deleteButton);

        list.appendChild(li);
    });
}

// Функція для видалення збірки
function deleteBuild(buildId) {
    showCustomConfirm('Ви дійсно хочете видалити цю збірку?', function (confirmed) {
        if (confirmed) {
            // Видалення з масиву
            savedBuilds = savedBuilds.filter(build => build.id !== buildId);
            localStorage.setItem('savedBuilds', JSON.stringify(savedBuilds));
            updateSavedBuildsUI(); // Оновити список
        }

        savedBuilds.forEach(build => {
            const li = document.createElement('li');
            li.textContent = `${build.name} – Енергоспоживання: ${build.totalPower} Вт`;
            li.dataset.id = build.id;
        
            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'Видалити';
            deleteButton.className = 'delete-button';
            deleteButton.onclick = function () {
                deleteBuild(build.id);
            };
        
            li.appendChild(deleteButton);
            list.appendChild(li);
        });
        
    });
}


// Закриття модального вікна
document.querySelector('.close-modal').addEventListener('click', () => {
    document.getElementById('build-details-modal').style.display = 'none';
});
window.addEventListener('click', (event) => {
    const modal = document.getElementById('build-details-modal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});

document.getElementById('save-build-button').addEventListener('click', () => {
    console.log('Кнопка "Зберегти збірку" натиснута'); // Для перевірки
    const components = getSelectedComponents();
    const totalPower = calculateTotalPower();

    console.log('Вибрані компоненти:', components);
    console.log('Сумарне енергоспоживання:', totalPower);

    const buildName = prompt('Введіть назву збірки:', `Збірка ${savedBuilds.length + 1}`);
    if (buildName) {
        saveBuild(buildName, components, totalPower);
    }
});

// Розрахунок загального енергоспоживання
function calculateTotalPower() {
    const powerElements = ['cpu', 'gpu', 'ram', 'ssd', 'motherboard'];
    let totalPower = 0;

    powerElements.forEach(id => {
        const element = document.getElementById(id);
        if (element && element.selectedIndex >= 0) {
            const power = parseInt(element.options[element.selectedIndex]?.dataset.power || '0', 10);
            totalPower += power;
        }
    });

    return totalPower;
}

function showBuildDetails(buildId) {
    const build = savedBuilds.find(b => b.id === buildId);

    if (build) {
        console.log('Показ деталей збірки:', build); // Додайте це для перевірки
        const modal = document.getElementById('build-details-modal');
        const buildName = document.getElementById('build-name');
        const buildDetails = document.getElementById('build-details');

        buildName.textContent = build.name;
        buildDetails.innerHTML = `
            <li><strong>Енергоспоживання:</strong> ${build.totalPower} Вт</li>
            <li><strong>Процесор:</strong> ${build.components.CPU}</li>
            <li><strong>Відеокарта:</strong> ${build.components.GPU}</li>
            <li><strong>Оперативна пам'ять:</strong> ${build.components.RAM}</li>
            <li><strong>Материнська плата:</strong> ${build.components.Motherboard}</li>
            <li><strong>Накопичувач:</strong> ${build.components.SSD}</li>
        `;

        modal.style.display = 'flex';
    }
}

// Функція для показу кастомного вікна підтвердження
function showCustomConfirm(message, onConfirm) {
    const modal = document.getElementById('custom-confirm-modal');
    const messageElement = document.getElementById('custom-confirm-message');
    const okButton = document.getElementById('custom-confirm-ok');
    const cancelButton = document.getElementById('custom-confirm-cancel');

    // Встановити текст повідомлення
    messageElement.textContent = message;

    // Показати модальне вікно
    modal.style.display = 'flex';

    // Дії при натисканні OK
    okButton.onclick = function () {
        modal.style.display = 'none'; // Закрити модальне вікно
        onConfirm(true); // Виконати підтвердження
    };

    // Дії при натисканні Cancel
    cancelButton.onclick = function () {
        modal.style.display = 'none'; // Закрити модальне вікно
        onConfirm(false); // Відхилити дію
    };
}

// Додавання обробника подій для видалення збірки
document.getElementById('delete-build-button').addEventListener('click', function () {
    showCustomConfirm('Ви дійсно хочете видалити цю збірку?', function (confirmed) {
        if (confirmed) {
            console.log('Збірку видалено!');
            // Тут додавайте код для видалення збірки
        } else {
            console.log('Дія скасована.');
        }
    });
});