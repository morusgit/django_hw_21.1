# 23.2 Кеширование и работа с переменными окружения
Задание 1 Продолжаем работать с проектом. Установите брокер для кеширования Redis. Внесите необходимые настройки и проверьте работоспособность проекта с новыми настройками.

Задание 2 Настройте кеширование всего контроллера отображения данных относительно одного продукта.

Помните, что кеширование можно подключать не только в файле views.py, но и в файле маршрутизации urls.py. Важно делать всё в одном месте, чтобы достичь единообразия в коде проекта и не запутаться впоследствии.

Задание 3 Создайте сервисную функцию, которая будет отвечать за выборку категорий и которую можно переиспользовать в любом месте системы. Добавьте низкоуровневое кеширование для списка категорий.

Задание 4 Вынесите необходимые настройки в переменные окружения и настройте проект для работы с ними.

Дополнительное задание
Добавьте кеширование всего сайта целиком, при этом отключите от кеширования определенные контроллеры, которые отвечают за работу по заполнению продуктов и блога.

# 23.1 Права доступа
Задание 1 Продолжаем работать с проектом. Создайте группу для роли модератора и опишите необходимые доступы:

-может отменять публикацию продукта, -может менять описание любого продукта, -может менять категорию любого продукта. Недостающее поле признака публикации необходимо добавить таким образом, чтобы можно было определять статус продукта. Можно использовать BooleanField со значением False по умолчанию или CharField с указанием вариантов значений (choises). При этом по умолчанию должен быть вариант, который не предполагает публикацию продукта.

Задание 2 Реализуйте решение, которое проверит, что редактирование продукта доступно только его владельцу.

Дополнительное задание Выделите отдельную роль для пользователя контент-менеджера, который может управлять публикациями в блоге. Также не
забудьте реализовать проверки на то, что обычный пользователь или модератор из другого отдела не сможет ничего изменить
в разделе блога.

# 22.2 Аутентификация
Задание 1 Создайте новое приложение для работы с пользователем. Определите собственную форму для пользователя, при этом задайте электронную почту как поле для авторизации.

Также добавьте поля:

«Аватар», «Номер телефона», «Страна». Задание 2 В сервисе реализуйте функционал аутентификации, а именно:

регистрацию пользователя по почте и паролю; верификацию почты пользователя через отправленное письмо; авторизацию пользователя; восстановление пользователя на автоматически сгенерированный пароль. Задание 3 Закройте для анонимных пользователей все контроллеры, которые отвечают за работу с продуктами. При этом создаваемые продукты должны автоматически привязываться к авторизованному пользователю.

Не забудьте добавить поле для продуктов, через которое пользователь будет привязываться. Текущий авторизованный пользователь доступен в любом контроллере через self.request.user .

*Дополнительное задание Добавьте интерфейс редактирования профиля пользователя.


# 22.1 Формы
Задание 1 Продолжаем работать с проектом из предыдущего домашнего задания. Для модели продуктов реализуйте механизм CRUD, задействовав модуль django.forms .

Условия для пользователей:

могут создавать новые продукты; не могут загружать запрещенные продукты на платформу. Для исключения загрузки запрещенных продуктов реализуйте валидацию названия и описания продукта таким образом, чтобы нельзя было в них добавлять слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.

Задание 2 Добавьте новую модель «Версия», которая должна содержать следующие поля:

продукт, номер версии, название версии, признак текущей версии. При наличии активной версии реализуйте вывод в список продуктов информации об активной версии.

Задание 3 Для работы с версиями продукта добавьте реализацию работы с формами. При этом версия может быть внесена только в существующий продукт.

Все созданные формы нужно стилизовать так, чтобы они были в единой стилистике оформления всей платформы. Для этого можно воспользоваться методом init либо самостоятельно изучить пакет crispy-forms: https://pypi.org/project/django-crispy-forms/.

Дополнительное задание В один момент времени может быть только одна активная версия продукта, поэтому при изменении версий необходимо проверять, что пользователь в качестве активной версии указал только одну. В случае возникновения ошибки вернуть сообщение пользователю и попросить выбрать только одну активную версию.


# 21.1 FBV и CBV
-Задание 1 Продолжаем работать с проектом из предыдущего домашнего задания. Переведите имеющиеся контроллеры с FBV на CBV.

-Задание 2 Создайте новую модель блоговой записи со следующими полями:

заголовок, slug (реализовать через CharField), содержимое, превью (изображение), дата создания, признак публикации, количество просмотров. Для работы с блогом реализуйте CRUD для новой модели.

Slug — человекопонятный URL, представляет собой набор символов, которые можно прочитать как связные слова или предложения в адресной строке, служит уникальным идентификатором записи в рамках одной модели и состоит из безопасных для обработки запроса символов:

0-9 ,

a-z (обычно в нижнем регистре), символ
. З-адание 3 Модифицируйте вывод и обработку запросов, добавив следующую логику на уровне контроллеров:

при открытии отдельной статьи увеличивать счетчик просмотров; выводить в список статей только те, которые имеют положительный признак публикации; при создании динамически формировать slug name для заголовка; после успешного редактирования записи необходимо перенаправлять пользователя на просмотр этой статьи. -* Дополнительное задание Когда статья достигает 100 просмотров, отправлять себе на почту поздравление с достижением.

Примечание: для отправки писем рекомендуем использовать почтовый сервис Яндекс.

Дополнительное задание, помеченное звездочкой, выполнять желательно, но не обязательно.

# 20.2 Шаблонизация
Задание 1
Создайте новый контроллер и шаблон, которые будут отвечать за отображение отдельной страницы с товаром. На странице с товаром необходимо вывести всю информацию о товаре.

Для создания шаблонов используйте UI kit Bootstrap. При возникновении проблем возьмите за основу данный шаблон.

Задание 2
В созданный ранее шаблон для главной страницы выведите список товаров в цикле. Для единообразия выводимых карточек отображаемое описание обрежьте после первых выведенных 100 символов.

Задание 3
Из-за расширения количества шаблонов появляется слишком много повторяющегося кода, поэтому выделите общий (базовый) шаблон и также подшаблон с главным меню.

При необходимости можно выделить больше общих шаблонов.

Задание 4
Для выводимого изображения на странице реализуйте шаблонный фильтр, который преобразует переданный путь в полный путь для доступа к медиафайлу:

<!-- Исходный вариант --> 
<img src="/media/{{ object.image }}" />
<!-- Итоговый вариант -->
<img src="{{ object.image|mediapath }}" />

Реализуйте описанный функционал с помощью шаблонного тега:

<!-- Исходный вариант -->
<img src="/media/{{ object.image }}" />
<!-- Итоговый вариант -->
<img src="{% mediapath object.image %}" />

* Дополнительное задание
Добавьте функционал создания продукта через внешний интерфейс, не используя стандартную админку.
Реализуйте постраничный вывод списка продуктов.


# 20.1 Работа с ORM в Django
+Задание 1

Подключите СУБД PostgreSQL для работы в проекте. Для этого:

Создайте базу данных в ручном режиме. Внесите изменения в настройки подключения.

+Задание 2

В приложении каталога создайте модели:

Product, Category. Опишите для них начальные настройки.

+Задание 3

Для каждой модели опишите следующие поля:

Product: наименование, описание, изображение (превью), категория, цена за покупку, дата создания, дата последнего изменения. Category: наименование, описание. Для поля с изображением необходимо добавить соответствующие настройки в проект, а также установить библиотеку для работы с изображениями Pillow

+Задание 4

Перенесите отображение моделей в базу данных с помощью инструмента миграций. Для этого:

Создайте миграции для новых моделей. Примените миграции. Внесите изменения в модель категорий, добавьте поле created_at, примените обновление структуры с помощью миграций. Откатите миграцию до состояния, когда поле created_at для модели категории еще не существовало, и удалите лишнюю миграцию.

-Задание 5

Для моделей категории и продукта настройте отображение в административной панели. Для категорий выведите id и наименование в список отображения, а для продуктов выведите в список id, название, цену и категорию. При этом интерфейс вывода продуктов настройте так, чтобы можно было результат отображения фильтровать по категории, а также осуществлять поиск по названию и полю описания.

-Задание 6

Через инструмент shell заполните список категорий, а также выберите список категорий, применив произвольные рассмотренные фильтры. В качестве решения приложите скриншот. Сформируйте фикстуры для заполнения базы данных. Напишите кастомную команду, которая умеет заполнять данные в базу данных, при этом предварительно зачищать ее от старых данных. Последний пункт можно реализовать в связке с инструментом работы с фикстурами, можно описать вставку данных отдельными запросами.

-* Дополнительное задание

В контроллер отображения главной страницы добавьте выборку последних 5 товаров и вывод их в консоль. Создайте модель для хранения контактных данных и попробуйте вывести данные, заполненные через админку, на страницу с контактами.

# 19.2 Знакомство с Django

Задание 1 Для начала работы над задачей выполните первые шаги:

Настройте виртуальное окружение. Создайте новый Django-проект. Задание 2 После успешного создания проекта сделайте первую настройку. Для этого:

Создайте первое приложение с названием catalog. Внесите начальные настройки проекта. Сделайте настройку урлов (URL-файлов) для нового приложения. Задание 3 Подготовьте два шаблона для домашней страницы и страницы с контактной информацией.

Для создания шаблонов лучше использовать UIkit Bootstrap. Это удобный набор элементов, которые уже стилизованы и готовы к использованию. UIkit Bootstrap помогает избежать самостоятельной верстки макетов.

Если возникнут проблемы при создании собственного интерфейса, возьмите за основу данный шаблон: https://github.com/oscarbotru/.

Задание 4 В приложении в контроллере реализуйте два контроллера:

Контроллер, который отвечает за отображение домашней страницы. Контроллер, который отвечает за отображение контактной информации.

Дополнительное задание Реализуйте обработку сбора обратной связи от пользователя, который зашел на страницу контактов и отправил свои данные для обратной связи.
Дополнительное задание, помеченное звездочкой, желательно, но не обязательно выполнять.

Критерии выполнения заданий Всё итоговое решение залили в github.com и сдали в виде ссылки на репозиторий. Создали отдельное приложение. Реализовали два контроллера. Адреса описали не внутри главного URL-файла, а вынесли в пространства имен. Добавили папку с шаблонами, в которой лежат два шаблона.