# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.open_groups_page()
    app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count()
    new_groups = db.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert old_groups == new_groups
    if check_ui:
        # groups_name_from_db = db.get_list_of_groups_names_and_ids()
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)