import logging

from marshmallow import ValidationError
from nameko.exceptions import BadRequest
from nameko.rpc import RpcProxy
from werkzeug import Response

from admin_gateway.entrypoints import http
# from admin_gateway.exceptions import CartNotFound
from admin_gateway.schemas import (BulkCreateCategories, BulkCreateDepartments,
                                   BulkCreateSectors, DepartmentSchema)


class AdminGatewayService(object):
    name = 'admin_gateway'

    admin_carts_rpc = RpcProxy('admin_carts')

    # ADMIN CARTS SERVICE ------------------------------------------------------------------------

    @http("GET", "/departments")
    def get_all_departments(self, _):
        result = self.admin_carts_rpc.get_all_departments()
        return Response(
            DepartmentSchema(many=True).dumps(result).data,
            mimetype='application/json'
        )

    @http("POST", "/departments", expected_exceptions=(ValidationError, BadRequest))
    def bulk_create_departments(self, request):
        schema = BulkCreateDepartments(strict=True)

        try:
            departments_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError:
            raise BadRequest("Invalid input")

        serialized_data = BulkCreateDepartments().dump(departments_data).data

        result = self.admin_carts_rpc.bulk_create_departments(serialized_data['names'])
        return Response(
            DepartmentSchema(many=True).dumps(result).data,
            mimetype='application/json'
        )

    @http("POST", "/sectors", expected_exceptions=(ValidationError, BadRequest))
    def bulk_create_sectors(self, request):
        schema = BulkCreateSectors(strict=True)

        try:
            sectors_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError:
            raise BadRequest("Invalid input")

        serialized_data = BulkCreateSectors().dump(sectors_data).data

        result = self.admin_carts_rpc.bulk_create_sectors(
            serialized_data['department_id'],
            serialized_data['names']
        )
        return Response(
            DepartmentSchema(many=True).dumps(result).data,
            mimetype='application/json'
        )

    @http("POST", "/categories", expected_exceptions=(ValidationError, BadRequest))
    def bulk_create_categories(self, request):
        schema = BulkCreateCategories(strict=True)

        try:
            categories_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError:
            raise BadRequest("Invalid input")

        serialized_data = BulkCreateCategories().dump(categories_data).data

        result = self.admin_carts_rpc.bulk_create_categories(
            serialized_data['sector_id'],
            serialized_data['names']
        )
        return Response(
            DepartmentSchema(many=True).dumps(result).data,
            mimetype='application/json'
        )
