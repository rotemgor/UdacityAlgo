class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    temp_users_list=group.get_users()
    if user in temp_users_list:
        print('Hi')
        return True
    else:
        if  len(group.get_groups())>0:
            group_list=group.get_groups()
            print(group_list)
            for temp_group in group_list:
                print(temp_group.get_name())
                return is_user_in_group(user, temp_group)
        else: # nosubgroups
            print("reached else")
            return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_us"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
print(is_user_in_group("sub_child_user", child))

