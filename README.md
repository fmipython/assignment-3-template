# Задание 3 - APIs

## Условие на задачата

В директорията src/ има 1 файла main.py в който има 1 функция `create_app`.
Заданието е да имплементирате функционалностите специфицирани в doc comment-a.

За да стартирате тестовете локално ще ви е необходимо да имате [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). Този токен трябва да се запише в ENV variable `GITHUB_TOKEN`. За улеснение на процеса ако използвате Gitpod може да използвате командата `just set-gh-token`. Вторият вариант за стартиране на тестовете е да подадете токена си директно на pytest `python -m pytest --token ghp_...`

За заданието ще ви е полезна [документацията на Flask](https://flask.palletsprojects.com/en/2.2.x/).
Както и документацията на [GitHub Api](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28).

Hints:
* Flask [работи на няколко нишки](https://stackoverflow.com/questions/19277280/preserving-global-state-in-a-flask-application). Това означава че ако имате глобални променливи те трябва да са защитени срещу конкурентен достъп.
* Фактът че има един src файл, не означава че той трябва да съдържа целия код :)

## Работа със заданието
Препоръчваме използвамето на [Gitpod](https://www.gitpod.io/), за който има автоматична конфигурация на средата.

В противен случай препоръчваме работа UNIX машина (или linux subsystem for windows)

Тези 2 инструмента улесняват работата по задачата (ако не ги ползвате ще трябва да създадете ръчно virtualenv и да пускате тестовете с `python -m pytest`):
- [just](https://github.com/casey/just)
- [direnv](https://direnv.net/)

### Използване на direnv:
В директорията на проекта трябва да включите direnv
```
$ direnv allow
```

### Използване на just
В директорията на проекта може да използвате:

```
$ just test # run all tests
```

```
$ just coverage # generate coverage information for the code
```

```
$ just coverage-html # generate coverage information in a html page (highlighting (un)covered lines)
```

```
$ just lint # Run the linter
```

## Предистория/Мотивация

Създаването на API е една от най-честите задачи.
Python е доста удобен инструмент за целта заради широкия набор от библиотеки.

В задачата ще имплементираме Proxy API към GitHub.
Целта е да не имплементираме твърде сложна логика, а да се фокусираме върху работата с API-и.
GitHub API има добри практики за работа и много подробна документация, което трябва да улесни работата.
Заданието покрива доста от основните проблеми при работа с API-и като аутентикация, работа с хедъри/параметри,
обработка на данни, засичане на метрики, и тн.

За повечето API-и се използват библиотеки за мониторинг като Prometheus.
Тези библиотеки(системи) са доста полезни за да знаем кога нашата система върви и кога не.
Но, са доста сложни и обемни.
Затова в заданието ще си имплементираме някои основни функционалности за мониторинг на ендпойнтите.
