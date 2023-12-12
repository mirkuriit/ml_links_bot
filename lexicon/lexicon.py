info_commands = ["/matStat", "/linAlg",
                 "/therVer", "/matAnal",
                 "/classicMl", "/introToNn",
                 "/deepLearning"]

phraces = {
    "start" : "Шпаргалка с полезными материалами для машинного обучения.\n" +
              "Автор: @mirkuriit",
    info_commands[0][1:]+"Command" : "КНИГИ: \n"
                                     "Статистика и котики [] - https://vk.com/doc-50757966_526114641?hash=iWS769JUsKq2U8vis2rJNgJUCBceRoVjjZ7cdZpOB5k&dl=DLvDnKLSvRpdfzYUtRXHTGlNl0Ahv1tcAFgWv6FEOz8 \n\n"
                                     "Практическая статистика для специалистов Data Science [2022] Питер Брюс, Питер Гедек, Эндрю Брюс - https://batrachos.com/sites/default/files/pictures/Books/Bruce_Bruce_2018_Practical%20Statistics%20for%20Data%20Scientists.pdf \n\n"
                                     "Статистика для чайников, Дебора Рамси, [2008] - https://djvu.online/file/23SRRmTDKylyb?ysclid=lpz74g3znv779414780 \n\n",
    info_commands[1][1:]+"Command" : "КУРСЫ/ПЛЕЙЛИСТЫ: \n"
                                     "суть линейной алгебры - https://www.youtube.com/watch?v=RNTRYicPvWQ&list=PLVjLpKXnAGLXPaS7FRBjd5yZeXwJxZil2 \n\n"
                                     "КНИГИ: \n"
                                     "Прикладная линейная алгебра для исследователей данных, Коэн M. И., [2023] https://vk.com/doc425072881_663231659?hash=rzymzCDqWOk5uG7pTHv0PMB5DwLymonHDaJu8d9fQC8&dl=j4z0WpJjqNueziZNoUzG2ebsghz2jpaZeoLfle3SayT \n\n"
                                     "Introduction to Linear Algebra, Gilbert Strang, [2016] https://vk.com/doc255577237_590062256?hash=ziykZkZepRzBqKKEwkZI4nNsWvO2XUnnl7KQcpGsRED&dl=Og8c0RsZ0KgGNG5cUaMTcSbJC8zZcjDzQWUtSCz8KNL \n\n",
    info_commands[2][1:]+"Command" : "КНИГИ: \n"
                                     "Теория вероятностей и математическая статистика Н.Ш.Кремер [2008] https://vk.com/doc44301783_561020939?hash=D8SvkpgljGAaNfW8p3zCr4xsJ7c9zrgoZ89QVpodMZw&dl=UcEvzby6Xv51mwzGCtBhBezKCLBjbEkO5KG3vnxHVjo \n\n"
                                     "Методичка от нижегородского госа https://fedorsarafanov.github.io/materials/var.pdf?ysclid=lpz86l8nhn529332852 \n\n"
                                     "КУРСЫ: \n"
                                     "https://stepik.org/course/2911/promo#toc \n"
                                     "https://stepik.org/course/3209/promo#toc \n"
                                     "https://stepik.org/course/3089/syllabus",
    info_commands[3][1:]+"Command" : "КНИГИ: \n"
                                     "Математический анализ, 1 том В.А.Зорич https://vk.com/doc530551121_611241130?hash=Bu3PtnLUZmXRyQtaC8xE7N2b6uFjlLftXoCN2PEU0gL \n\n"
                                     "Математический анализ, 2 том В.А.Зорич https://vk.com/doc530551121_611241160?hash=vtASAQBmNO8g0Xbg902nq3gFOU7QxlkIzEloObzNeNP \n\n"
                                     "ПЛЕЙЛИСТЫ/КУРСЫ: \n"
                                     "Суть матанализа - youtube.com/watch?v=qd0rzmSGPWg&list=PLVjLpKXnAGLVbrcJdDb0a2RS6MmRCgxJz",
    info_commands[4][1:]+"Command" : "КУРСЫ: \n"
                                     "Открытый курс по машинному обучению от ods - https://habr.com/ru/companies/ods/articles/322626/ \n"
                                     "Видеолекции по вышестоящему курсу - https://www.youtube.com/watch?v=OAy96yiWohk&list=PLVlY_7IJCMJdgcCtQfzj5j8OVB_Y0GJCl \n\n"
                                     "КНИГИ: \n"
                                     "Введение в машинное обучение с помощью Python А. Мюллер, С. Гвидо [2017] - https://vk.com/doc68607069_450673291?hash=ZzLPku2KUhFIhpcQJyANzrCSzkV6CgA8ah9tF065iy8 \n\n"
                                     "Grokking Machine Learning Serrano G. Luis [2020]"
                                     "ДРУГОЕ: \n"
                                     "Статьи по машинному обучению на хабре - https://habr.com/ru/hubs/machine_learning/articles/"
                                     "",
    info_commands[5][1:]+"Command" : "КНИГИ: \n"
                                     "Грокаем глубокое обучение [2019] Эндрю Траск - https://vk.com/doc10943591_564416471?hash=Iry5n5GQiilUaR87Uf0HJVc5sQZd2a2Z2FLBCnv6wC0 \n\n"
                                     "Создаём нейронную сеть [2017] Автор Тарик Рашид - https://vk.com/doc10943591_580719118?hash=RwVGwKYV19ZdazSwzNZyzy9wPABDxqd2zMr5PPVQpMX \n\n"
                                     "КУРСЫ/ПЛЕЙЛИСТЫ: \n"
                                     "Суть глубокого обучения - https://www.youtube.com/watch?v=RJCIYBAAiEI&list=PLZjXXN70PH5itkSPe6LTS-yPyl5soOovc",
    info_commands[6][1:]+"Command" : "КНИГИ: \n"
                                     "Глубокое обучение с подкреплением: теория и практика на языке Python [2022] Грессер Л., Кенг В. - https://t.me/physics_lib/9438 \n\n"
                                     "PyTorch. Освещая глубокое обучение - https://coderbooks.ru/books/python/pytorch_osveshchaya_glubokoe_obuchenie_stivens_2022/ \n\n"
                                     "КУРСЫ/ПЛЕЙЛИСТЫ: \n"
                                     "1) ИИ Старт (последняя часть курса) - https://stepik.org/course/125587/syllabus \n\n"
                                     "2) ИИ Старт продвинутый уровень - https://stepik.org/course/134942/syllabus"

}