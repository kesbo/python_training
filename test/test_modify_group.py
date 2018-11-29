from model.group import Group
from random import randrange


def test_modifay_group_name(app, db, check_ui):
    app.group.open_groups_page()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test group for modifying"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group name", header="Modified header", footer="Modified footer")
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert old_groups == new_groups
    if check_ui:
        groups_name_from_db = db.get_list_of_groups_names_and_ids()
        assert sorted(groups_name_from_db, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)