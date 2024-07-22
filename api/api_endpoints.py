from api import ApiManager
from source_shop import ApiLinks


class ApiEndpoints(ApiManager):

    def post_submit_order(self, quantity, package_id):
        body = {
            "quantity": quantity,
            "package_id": package_id,
        }
        response = self.post(url=ApiLinks.order_url, body=body)
        assert response.status_code == 200, "Order submission failed"
        return response

    def get_sims(self):
        response = self.get(url=f'{ApiLinks.sims_url}?include=order%2Corder.status%2Corder.user&limit=6')
        assert response.status_code == 200, "Get orders failed."
        return response
