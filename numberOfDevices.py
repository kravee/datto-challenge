def numberOfDevices(connections, toggleIps):
    '''
    the function return number of connection devices to single ip.
    for example:
    connections=[["192.167.0.0","192.167.0.1"],["192.167.0.2","192.167.0.0"],["192.167.0.0","192.167.0.3"]]
    toggleIps =["192.167.0.1","192.167.0.0","192.167.0.2","192.167.0.0","0.0.0.0"]
    the output will be [0, 1, 1, 2, 0]
    "192.167.0.1" would become active and is a part of connection ["192.167.0.0","192.167.0.1"], howewer no other devices active => 0
    "192.167.0.0" would become active and is a part of connection ["192.167.0.0","192.167.0.1"] "192.167.0.1" already active => 1
    "192.167.0.2" would become active and is a part of connection ["192.167.0.2","192.167.0.0"] "192.167.0.0" already active => 1
    "192.167.0.0" would become inactive is exist in 2 connection => 2
    "0.0.0.0" would become active, no connection => 0
    :param connections: list of connection IP pair
    :param toggleIps: sequence of single IP
    :return: list of connection to each single IP
    '''
    class ip_connection:
        '''
        each device will have object with 3 variable
        ip
        active
        list of connected devices
        '''
        active = 0
        def __init__(self, ip_address, connection_list):
            self._ip_address = ip_address
            self._connection_list = connection_list

        def connection_list(self):
            return self._connection_list

        def ip_address(self):
            return self._ip_address

    def deviceConnectivityMap(connections, toggleIps):
        '''
        The function get connection and ip, will build list of object, each one will have 3 variable
        device IP
        active => 1/0
        list of connected devices
        :param connections: list 2x2 of connected devices
        :param toggleIps: list
        :return: list of object
        '''
        list_ip = []
        uniqtoggleIps = list(dict.fromkeys(toggleIps))
        for i in uniqtoggleIps:
            device_ip = i
            connectin_list = []
            for y in connections:
                if y[0] == device_ip or y[1] == device_ip:
                    if y[0] == device_ip:
                        connectin_list.append(y[1])
                    else:
                        connectin_list.append(y[0])
            device_data = ip_connection(device_ip,connectin_list)
            list_ip.append(device_data)

        return list_ip

    def connectionNumber(deviceConnection, allDevices):
        '''
        The function get list of connected devices to relevant device and list of object with all devices in network
        Will return the number ok connected devices only to relevant device
        :param deviceConnection: list of all connected devices
        :param allDevices: list of alldevices(class)
        :return: int
        '''

        connection = 0
        for i in deviceConnection:
            for y in allDevices:
                if i == y.ip_address():
                    connection += y.active
        return connection

    result = []
    numberActiveConnection = 0

    deviceMap = deviceConnectivityMap(connections,toggleIps)

    for i in toggleIps:
        for y in deviceMap:
            if i == y.ip_address():
                numberActiveConnection = connectionNumber(y.connection_list(), deviceMap)
                if y.active == 0:
                    y.active = 1
                else:
                    y.active = 0
        result.append(numberActiveConnection)


    return result

# Driver program
if __name__ == "__main__":
    connections=[["192.167.0.0","192.167.0.1"],["192.167.0.2","192.167.0.0"],["192.167.0.0","192.167.0.3"]]
    toggleIps =["192.167.0.2", "192.167.0.0"]
    print(numberOfDevices(connections, toggleIps))