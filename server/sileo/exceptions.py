
class APIException(Exception):
    """ Base Exception class for all api exceptions that's code in sileo """

    DEFAULT_DETAIL = ''
    DEFAULT_STATUS = 404
    DEFAULT_CODE = ''

    def __init__(self, extras=None, **kwargs):
        """ Initialize the exception with all needed information
        Arguments:
            * status - The status code you want in the response when the
                exception is raised
            * detail - The details explaining why the exception is raised. This
                will be part of the response data.
            * code (optional) - The error code for this type of exceptions. An
                example would be 'permission_denied'. Error codes should be
                used to allow more readable error handle code in the consumer
            * extras (optional) - A json serializable dict used for passing
                additional data sent in the response when the error is raised
        """
        self.detail = kwargs.get('detail', self.DEFAULT_DETAIL)
        self.status = kwargs.get('status', self.DEFAULT_STATUS)
        self.code = kwargs.get('code', self.DEFAULT_CODE)
        if extras:
            self.extras = extras
        else:
            self.extras = self._get_default_extras()
        super(APIException, self).__init__(self.detail)

    def _get_default_extras(self):
        """ Returns a default extra context sent to the http response. This is
        in the form a function to make sure issues on pass by reference is
        avoided.
        """
        return {}

    def get_full_details(self):
        """ Returns a serializable dict that's ready to be sent as the message
        for the http response.
        """
        if 'detail' not in self.extras:
            self.extras['detail'] = self.detail
        if 'code' not in self.extras:
            self.extras['code'] = self.code
        return self.extras

    def get_context(self):
        """ This method will return a dict representing the error formatted in
        a way that the sileo view can easily handle
        """
        return {
            'status_code': self.status,
            'data': self.get_full_details()
        }


class PermissionDenied(APIException):
    """ Exception raised when the user trying to access the resource do not
    have the right permission. e.g. he/she does not own the instance etc.
    """
    DEFAULT_DETAIL = 'You do not have permission to access the resource.'
    DEFAULT_CODE = 'permission_denied'
    DEFAULT_STATUS = 403


class NotFound(APIException):
    """ Exception raised when the object that the user is trying to get does not
    exist. A counterpart of django's HTTP404 exception.
    """
    DEFAULT_DETAIL = 'Object not found.'
    DEFAULT_CODE = 'object_not_found'
    DEFAULT_STATUS = 404


class MethodNotSupported(APIException):
    """ Exception raised when the resource that the user is trying to access
    does support a method (filter, get, create, etc)
    """
    DEFAULT_DETAIL = 'The method you are trying to access is not supported ' +\
        'by the resource.'
    DEFAULT_CODE = 'method_not_supported'
    DEFAULT_STATUS = 404
