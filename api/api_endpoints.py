from api import ApiManager


class ApiEndpoints(ApiManager):

    def post_submit_order(self, quantity, package_id):
        body = {
            "quantity": quantity,
            "package_id": package_id,
        }
        response = self.post(url=f'https://sandbox-partners-api.airalo.com/v2/orders', body=body)
        assert response.status_code == 200, "Order submission failed"
        return response

    def get_sims(self):
        response = self.get(url=f'https://sandbox-partners-api.airalo.com/v2/orders')
        assert response.status_code == 200, "Get orders failed."
        return response
