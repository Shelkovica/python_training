from model.group import Group


def test_modify_group(app):
    app.group.modify_first_group(Group(name="test new", header="test2 new", footer="test3 new"))


def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="name new"))


def test_modify_first_group_footer(app):
    app.group.modify_first_group(Group(footer="footer new"))


def test_modify_first_group_header(app):
        app.group.modify_first_group(Group(header="header new"))
