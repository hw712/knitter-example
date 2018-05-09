from hobby.page import Hobby


def TestCase01_UserInformation():
    Hobby.User.Title.WaitForAppearing()

    Hobby.User.Title.VerifyEnabled(True)
    Hobby.User.Title.VerifyVisible(True)

    Hobby.User.Title.Select("Mrs.")
    Hobby.User.Title.VerifyAttribute("value", "Mrs.")

    Hobby.User.Title.SelectByOrder(3)
    Hobby.User.Title.VerifyAttribute("value", "Ms.")
    Hobby.User.Title.VerifyAttribute("value", "Dr.", assertion="not equal")

    Hobby.User.Name.Set("Super Man")
    Hobby.User.Name.VerifyAttribute("value", "Super", assertion="contain")
    Hobby.User.Name.VerifyAttribute("value", "More", assertion="not contain")
    Hobby.User.Name.VerifyAttribute("value", "Here Comes Super Man!!", assertion="in")


def TestCase02_Gender():
    Hobby.Gender.Male.VerifyAttribute("checked", None)
    Hobby.Gender.Female.VerifyAttribute("checked", None)

    Hobby.Gender.Male.Click()
    Hobby.Gender.Male.VerifyAttribute("checked", "true")
    Hobby.Gender.Female.VerifyAttribute("checked", None)

    if Hobby.Gender.Female.IsAttribute("checked", None, assertion="equal"):
        Hobby.Gender.Female.Click()

        Hobby.Gender.Female.VerifyAttribute("checked", "true")
        Hobby.Gender.Male.VerifyAttribute("checked", None)
    else:
        raise AssertionError("Female should be un-checked!")


def TestCase03_Hobbies():
    Hobby.Hobby.Music.VerifyAttribute("checked", None)
    Hobby.Hobby.Sport.VerifyAttribute("checked", None)
    Hobby.Hobby.Travel.VerifyAttribute("checked", None)

    Hobby.Hobby.Music.Click()
    Hobby.Hobby.Travel.Click()

    Hobby.Hobby.Music.VerifyAttribute("checked", "true")
    Hobby.Hobby.Sport.VerifyAttribute("checked", None)
    Hobby.Hobby.Travel.VerifyAttribute("checked", "true")

    Hobby.Hobby.Travel.Click()
    Hobby.Hobby.Travel.VerifyAttribute("checked", None)


def TestCase04_SelectionResult():
    Hobby.Result.VerifyAttribute("innerHTML", "")

    Hobby.User.Title.SelectByOrder(1)
    Hobby.User.Name.Set("Super Man")

    Hobby.Gender.Male.Click()

    Hobby.Hobby.Music.Click()
    Hobby.Hobby.Sport.Click()

    Hobby.SubmitButton.Click()

    Hobby.Result.VerifyAttribute("innerHTML", "Sport", assertion="contain")
    Hobby.Result.VerifyAttribute("innerHTML", "Male", assertion="contain")
    Hobby.Result.VerifyAttribute("innerHTML", "Female", assertion="not contain")
    Hobby.Result.VerifyAttribute("innerHTML", "Travel", assertion="not contain")


def TestCase05_ThisOneShouldFail():
    Hobby.Result.VerifyAttribute("innerHTML", "")

    Hobby.User.Title.SelectByOrder(1)
    Hobby.User.Name.Set("Super Man")

    Hobby.Gender.Male.Click()

    Hobby.Hobby.Music.Click()
    Hobby.Hobby.Sport.Click()

    Hobby.SubmitButton.Click()

    Hobby.Result.VerifyAttribute("innerHTML", "Sport", assertion="not contain")
    Hobby.Result.VerifyAttribute("innerHTML", "Male", assertion="not contain")
    Hobby.Result.VerifyAttribute("innerHTML", "Travel", assertion="not contain")
