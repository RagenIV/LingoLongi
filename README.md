# LingoLongi
This app helps learn unknown words from movies

Пока доступна только backend версия.
Чтобы установить программу, нужно скачать и распаковать репозиторий, установить зависимости
- nltk
- xlwings
и запустить LingoLongi.py, далее следовать инструкциям.

Программа
1) подгрузит субтитры из файла srt/twilight.srt,
2) лемматизирует слова,
3) запросит уровнь знания языка,
4) отфильтрует незнакомые слова,
5) спросит, сколько из найденных слов вывести для дальнейшего изучения
6) выведет их

В разработке
1) автоматическая выгрузка субтитров с сайта my-subs.co по запросу пользователя,
2) полноценная нормализация слова (не простая стеммизация или лемматизация),
3) определение уровня по предварительному тестированию,
4) создание индивидуальной модели вокабуляра,
5) определение степени информативности и оторванности от контекста незнакомых слов,
6) составление индивидуальной траектории просмотра.
