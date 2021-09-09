"""List Methods"""

def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue:  list - names in the normal queue.
    :param ticket_type:  int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """
    if ticket_type == 1:
        express_queue.append(person_name)
        updated_queue = express_queue
    elif ticket_type == 0:
        normal_queue.append(person_name)
        updated_queue = normal_queue
    else:
        raise ValueError('Invalid ticket type.')

    return updated_queue


def find_my_friend(queue, friend_name):
    """

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """
    if friend_name in queue:
        friend_index = queue.index(friend_name)
    else:
        raise ValueError('Friend not in queue.')

    return friend_index


def add_me_with_my_friends(queue, index, person_name):
    """

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """
    return queue[:index] + [person_name] + queue[index:]


def remove_the_mean_person(queue, person_name):
    """

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return:  list - queue update with the mean persons name removed.
    """
    if person_name in queue:
        queue.remove(person_name)
        updated_queue = queue
    else:
        raise ValueError('Mean person not in queue.')

    return updated_queue

def how_many_namefellows(queue, person_name):
    """

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return:  int - the number of times the name appears in the queue.
    """
    return queue.count(person_name)


def remove_the_last_person(queue):
    """

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    return queue.pop(-1)


def sorted_names(queue):
    """

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """
    return sorted(queue)
