from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="test new", header="test2 new", footer="test3 new"))
    app.session.logout()


def test_modify_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="name new"))
    app.session.logout()


def test_modify_first_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(footer="footer new"))
    app.session.logout()


def test_modify_first_group_header(app):
        app.session.login(username="admin", password="secret")
        app.group.modify_first_group(Group(header="header new"))
        app.session.logout()