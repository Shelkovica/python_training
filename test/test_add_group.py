# -*- coding: utf-8 -*-
import allure

from model.group import Group
import pytest

def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    group_list = my_step_1(app, db)
    my_step_2(app, group)
    my_step_3(app, check_ui, db, group, group_list)

@allure.step("Given a group list")
def my_step_1(app, db):
    old_groups = db.get_group_list()
    return old_groups

@allure.step("Add a group to the list")
def my_step_2(app, group):
    app.group.create(group)

@allure.step("Assert group list")
def my_step_3(app, check_ui, db, group,  old_groups):
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
