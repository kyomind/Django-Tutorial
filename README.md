![Kyo's Django Tutorial](https://i.imgur.com/D4mTT4l.png)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-blue?labelColor=444&logo=pre-commit)](https://github.com/pre-commit/pre-commit)
![](https://img.shields.io/codecov/c/github/kyomind/kyo-django-tutorial?labelColor=444&logo=codecov&color=blue)

這個倉庫是我 [Django 系列教學文章](https://blog.kyomind.tw/categories/Django/)的**實作參考程式碼**，目前文章預計如下：
## Django ORM 系列
1. [Django ORM：一對一、一對多外鍵教學（上）前言與關聯設定](https://blog.kyomind.tw/django-models/)
2. Django ORM：一對一、一對多外鍵教學（下）常用查詢

## Django × pytest：API 單元測試入門系列
1. Django 測試指南：用 pytest 撰寫 API 單元測試——環境設定篇
2. Django 測試指南：用 pytest 撰寫 API 單元測試——Fixtures 篇
3. Django 測試指南：使用 pytest + pytest-cov 計算 Test Coverage

## 分支說明

每一個分支格式如下：

```
01-django-models
```

其中 `01` 代表**文章發表的順序**編號，`django-models` 代表文章網址 slug，分支內容為該文章所新增的程式碼。

分支主要作為歷史記錄之用，但有些特殊情況的程式碼，可能也需要使用特定的分支保留。一般言而，分支會在文章發佈後，合併到 `main` 。
