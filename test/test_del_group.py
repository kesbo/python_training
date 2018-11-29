from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    app.group.open_groups_page()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test group for deleting"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        # groups_name_from_db = db.get_list_of_groups_names_and_ids()
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
