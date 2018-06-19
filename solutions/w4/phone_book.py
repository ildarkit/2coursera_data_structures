# python3


INIT_RESPONSE = 'not found'


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def init_contacts(max_phone_digits=10 ** 7):
    """
    A direct addressing scheme is used to store contacts.
    :return: list of contacts
    """
    contacts = []
    for i in range(max_phone_digits):
        contacts.append(INIT_RESPONSE)
    return contacts


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = init_contacts()
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name

            contacts[cur_query.number] = cur_query.name

        elif cur_query.type == 'del':
            contacts[cur_query.number] = INIT_RESPONSE
        else:
            result.append(contacts[cur_query.number])
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
