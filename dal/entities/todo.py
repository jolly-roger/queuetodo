class todo(object):
    def __int__(self, id = -1, name = "", statusId = -1, statusName = "", isShared = false, priority = -1):
        self.id = id
        self.name = name
        self.statusId = statusId
        self.statusName = statusName
        self.isShared = isShared
        self.priority = priority