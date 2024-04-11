from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.db import connection
from django.db import OperationalError
def home(request):
    return render(request, 'home.html')

def get_auction_sql(request):
    ''' Using Raw SQL bypassing Model '''
    try:
        auctionID = request.GET.get('auctionID')
        if auctionID:
            cursor = connection.cursor()
            query = f"""
                        SELECT *
                        FROM Auction
                        WHERE AuctionID  = {auctionID}
                    """
            cursor.execute(query)
            auction = cursor.fetchall()
            auction_details = [
                {
                    'AuctionID': row[0],
                    'VIN': row[1],
                    'Status': row[2],
                    'StartPrice': row[3],
                    'HighestPrice': row[4],
                    'SellerID': row[5],
                    'BuyerID': row[6],
                    'StartDate': row[7],
                    'EndDate': row[8]
                }
                for row in auction
            ]


            context = {
                'auction_details': auction_details
            }

            return render(request, '1_get_auction_details.html', context)
        else:
            # Handle the case where auctionID4 is None or not provided
            return render(request, 'error.html')
    except OperationalError as e:
        error_message = str(e)
        return render(request, 'error.html', {'error_message': error_message})

    except Exception as e:
        error_message = "An unexpected error occurred: " + str(e)
        return render(request, 'error.html', {'error_message': error_message})


def get_popular_car_sql(request):

    try:
        cursor = connection.cursor()
        query = f"""
                WITH tmp2 AS (
                SELECT a.VIN, 
                       COUNT(b.BidID) AS BidNum, 
                       DENSE_RANK() OVER(ORDER BY COUNT(b.BidID) DESC) AS NumBidsRnk
                FROM Bid b INNER JOIN Auction a ON b.AuctionID = a.AuctionID
                GROUP BY a.VIN)
                SELECT 
                    VIN,
                    BidNum
                FROM tmp2
                WHERE NumBidsRnk = 1;
                   """
        cursor.execute(query)
        car = cursor.fetchall()
        car_details = [
            {
                'VIN': row[0],
                'BidNum': row[1]
            }
            for row in car
        ]

        context = {
            'car_details': car_details
        }

        return render(request, '2_get_popular_car.html', context)
    except OperationalError as e:
        error_message = str(e)
        return render(request, 'error.html', {'error_message': error_message})

    except Exception as e:
        error_message = "An unexpected error occurred: " + str(e)
        return render(request, 'error.html', {'error_message': error_message})

def get_vin_car_sql(request):
    try:
        VIN = "'" + request.GET.get('VIN') + "'"
        cursor = connection.cursor()
        query = f"""
                SELECT *
                    FROM Bid b INNER JOIN Auction a ON b.AuctionID = a.AuctionID
                    WHERE VIN = {VIN};
                   """
        cursor.execute(query)
        car = cursor.fetchall()
        vin_car_details = [
            {
                'BidID': row[0],
                'BidderID': row[1],
                'AuctionID': row[2],
                'Amount': row[3],
                'Timestamps': row[4],
                'IsWin': row[5],
                'AuctionID': row[6],
                'VIN': row[7],
                'Status': row[8],
                'StartPrice': row[9],
                'HighestPrice': row[10],
                'SellerID': row[11],
                'BuyerID': row[12],
                'StartDate': row[13],
                'EndDate': row[14]
            }
            for row in car
        ]

        context = {
            'vin_car_details': vin_car_details
        }

        return render(request, '3_get_vin_car.html', context )
    except OperationalError as e:
        error_message = str(e)
        return render(request, 'error.html', {'error_message': error_message})

    except Exception as e:
        error_message = "An unexpected error occurred: " + str(e)
        return render(request, 'error.html', {'error_message': error_message})

def get_buyer_product_sql(request):
    ''' Using Raw SQL bypassing Model '''
    try:
        auctionID4 = request.GET.get('auctionID4')

        if auctionID4:
            cursor = connection.cursor()
            query = f"""
                        SELECT *
                        FROM User
                        WHERE UserID IN (
                        SELECT BuyerID
                        FROM Auction
                        WHERE AuctionID = {auctionID4});
                    """
            cursor.execute(query)
            buyer = cursor.fetchall()
            buyer_details = [
                {
                    'UserID': row[0],
                    'FirstName': row[1],
                    'LastName': row[2],
                    'Email': row[3],
                    'Phone': row[4],
                    'Password': row[5],
                    'Address': row[6],
                    'UserType': row[7]
                }
                for row in buyer
            ]

            context = {
                'buyer_details': buyer_details
            }

            return render(request, '4_get_buyer_product.html', context)
        else:
            # Handle the case where auctionID4 is None or not provided
            return render(request, '4_get_buyer_product.html', {'buyer_details': []})
    except OperationalError as e:
        error_message = str(e)
        return render(request, 'error.html', {'error_message': error_message})

    except Exception as e:
        error_message = "An unexpected error occurred: " + str(e)
        return render(request, 'error.html', {'error_message': error_message})

def get_user_inform_sql(request):
    try:
        userID = request.GET.get('userID5')
        cursor = connection.cursor()
        query = f"""
                SELECT *
                FROM Buyer AS B LEFT JOIN User AS U ON B.BuyerID = U.UserID
                WHERE UserID = {userID};
                """
        cursor.execute(query)
        user = cursor.fetchall()
        user_details = [
            { 'BuyerID': row[0],
        'BuyCarNum': row[1],
        'BidNum': row[2],
        'UserID': row[3],
        'FirstName': row[4],
        'LastName': row[5],
        'Email': row[6],
        'Phone': row[7],
        'Password': row[8],
        'Address': row[9],
        'UserType': row[10]}
            for row in user
    ]
        context = {
            'user_details': user_details
        }

        return render(request, '5_get_user_inform.html', context )
    except OperationalError as e:
        error_message = str(e)
        return render(request, 'error.html', {'error_message': error_message})

    except Exception as e:
        error_message = "An unexpected error occurred: " + str(e)
        return render(request, 'error.html', {'error_message': error_message})

def get_time_report_sql(request):
    try:
        cursor = connection.cursor()
        query = f"""
                    SELECT *,
                    
                           Timestamps >= CURDATE() - INTERVAL 7 DAY as OneWeek, -- if bid happended one week before
                           Timestamps >= CURDATE() - INTERVAL 14 DAY as TwoWeek,
                           MONTH(TimeStamps)  as Month,
                           YEAR(TimeStamps) as Year
                    FROM Bid
                """
        cursor.execute(query)
        report = cursor.fetchall()
        report_details = [
            {
                "BidID": row[0],
                "BidderID": row[1],
                "AuctionID": row[2],
                "Amount": row[3],
                "Timestamps": row[4],
                "IsWin": row[5],
                "OneWeek": row[6],
                "TwoWeek": row[7],
                "Month": row[8],
                "Year": row[9]

            }
            for row in report
    ]
        context = {
            'report_details': report_details
        }

        return render(request, '6_get_time_report.html', context )
    except OperationalError as e:
        error_message = str(e)
        return render(request, 'error.html', {'error_message': error_message})

    except Exception as e:
        error_message = "An unexpected error occurred: " + str(e)
        return render(request, 'error.html', {'error_message': error_message})


def get_car_inform_sql(request):
    try:
        VIN = "'" + request.GET.get('VIN7') + "'"
        cursor = connection.cursor()
        query = f"""
                SELECT *
                    FROM Car
                    WHERE VIN = {VIN};
                """
        cursor.execute(query)
        car = cursor.fetchall()
        car_details = [
            {
                "VIN": row[0],
                "Make": row[1],
                "Model": row[2],
                "Year": row[3],
                "Mileage": row[4],
                "Condition": row[5]
            }
            for row in car
    ]
        context = {
            'car_details': car_details
        }
        return render(request, '7_get_car_inform.html', context )
    except OperationalError as e:
        error_message = str(e)
        return render(request, 'error.html', {'error_message': error_message})

    except Exception as e:
        error_message = "An unexpected error occurred: " + str(e)
        return render(request, 'error.html', {'error_message': error_message})


def get_purchase_inform_sql(request):
    try:
        VIN = "'" + request.GET.get('VIN8') + "'"
        cursor = connection.cursor()
        query = f"""
                    SELECT *
                    FROM `Order`
                    WHERE VIN = {VIN}
                """
        cursor.execute(query)
        purchase = cursor.fetchall()
        purchase_details = [
            {   "OrderID": row[0],
                "AuctionID": row[1],
                "VIN": row[2],
                "Status": row[3],
                "Amount": row[4],
                "OrderDate": row[5]
            }
            for row in purchase
    ]
        context = {
            'purchase_details': purchase_details
        }
        return render(request, '8_get_purchase_inform.html', context )
    except OperationalError as e:
        error_message = str(e)
        return render(request, 'error.html', {'error_message': error_message})

    except Exception as e:
        error_message = "An unexpected error occurred: " + str(e)
        return render(request, 'error.html', {'error_message': error_message})


def get_review_inform_sql(request):
    try:
        SID = request.GET.get('SID9')
        cursor = connection.cursor()
        query = """
                SELECT Rating, Comment
                FROM `Order` as o LEFT JOIN Review ON o.OrderID = Review.OrderID
                WHERE VIN IN
                (SELECT VIN
                FROM Post
                WHERE SellerID = %s)
                """
        cursor.execute(query, [SID])
        review = cursor.fetchall()
        review_details = [
            {"Rating": row[0],
             "Comment": row[1]}
            for row in review
        ]
        context = {
            'review_details': review_details
        }
        return render(request, '9_get_review_inform.html', context)
    except OperationalError as e:
        error_message = str(e)
        return render(request, 'error.html', {'error_message': error_message})

    except Exception as e:
        error_message = "An unexpected error occurred: " + str(e)
        return render(request, 'error.html', {'error_message': error_message})



def filter_cars_sql(request):
    try:
        make = request.GET.get('make10')
        model = request.GET.get('model10')
        year = request.GET.get('year10')

        cursor = connection.cursor()
        query = "SELECT * FROM Car WHERE"
        params = []

        if make:
            query += " Make = %s"
            params.append(make)
        if model:
            if params:
                query += " AND"
            query += " Model = %s"
            params.append(model)
        if year:
            if params:
                query += " AND"
            query += " Year = %s"
            params.append(year)

        if not params:
            query = "SELECT * FROM Car"

        print('testing filter car sql query:')
        print(query)

        cursor.execute(query, params)
        filtered_cars = cursor.fetchall()

        car_details = [
            {
                'VIN': row[0],
                'Make': row[1],
                'Model': row[2],
                'Year': row[3],
                'Mileage': row[4],
                'Condition': row[5]
            }
            for row in filtered_cars
        ]

        context = {
            'car_details': car_details
        }

        return render(request, '10_filter_cars.html', context)
    except OperationalError as e:
        error_message = str(e)
        return render(request, 'error.html', {'error_message': error_message})

    except Exception as e:
        error_message = "An unexpected error occurred: " + str(e)
        return render(request, 'error.html', {'error_message': error_message})

def filter_cars_cont_sql(request):
    try:
        make = request.GET.get('make11')
        model = request.GET.get('model11')
        year = request.GET.get('year11')

        cursor = connection.cursor()
        query = "SELECT COUNT(VIN) AS NumCars FROM Car WHERE"
        params = []

        if make:
            query += " Make = %s"
            params.append(make)
        if model:
            if params:
                query += " AND"
            query += " Model = %s"
            params.append(model)
        if year:
            if params:
                query += " AND"
            query += " Year = %s"
            params.append(year)

        if not params:
            query = "SELECT COUNT(VIN) AS NumCars FROM Car"

        cursor.execute(query, params)
        filtered_cars = cursor.fetchall()

        car_details = [
            {
                'NumCars': row[0]
            }
            for row in filtered_cars
        ]

        context = {
            'car_cnt_details': car_details
        }

        return render(request, '11_filter_cars_cont.html', context)

    except OperationalError as e:
        error_message = str(e)
        return render(request, 'error.html', {'error_message': error_message})

    except Exception as e:
        error_message = "An unexpected error occurred: " + str(e)
        return render(request, 'error.html', {'error_message': error_message})


def filter_sellers_sql(request):
    try:
        saleCarNum = request.GET.get('SaleCarNum')

        cursor = connection.cursor()
        query = f"""
            SELECT *
            FROM Seller
            WHERE SaleCarNum > {saleCarNum};
        """

        cursor.execute(query)
        filtered_buyers = cursor.fetchall()

        sellers_details = [
            {
                'SellerID': row[0],
                'SaleCarNum': row[1]

            }
            for row in filtered_buyers
        ]

        context = {
            'sellers_details': sellers_details
        }
        return render(request, '12_filter_sellers.html', context)
    except OperationalError as e:
        error_message = str(e)
        return render(request, 'error.html', {'error_message': error_message})

    except Exception as e:
        error_message = "An unexpected error occurred: " + str(e)
        return render(request, 'error.html', {'error_message': error_message})

def filter_buyers_sql(request):
    try:
        buyCarNum = request.GET.get('BuyCarNum')

        cursor = connection.cursor()
        query = f"""
                SELECT *
                FROM Buyer
                WHERE BuyCarNum > {buyCarNum};
        """

        cursor.execute(query)
        filtered_buyers = cursor.fetchall()

        buyers_details = [
            {
                'BuyerID': row[0],
                'BuyCarNum': row[1],
                'BidNum': row[2]

            }
            for row in filtered_buyers
        ]

        context = {
            'buyers_details': buyers_details
        }
        return render(request, '13_filter_buyers.html', context)
    except OperationalError as e:
        error_message = str(e)
        return render(request, 'error.html', {'error_message': error_message})

    except Exception as e:
        error_message = "An unexpected error occurred: " + str(e)
        return render(request, 'error.html', {'error_message': error_message})

# def avg_sell_price_sql(request):
#     try:
#         make = request.GET.get('make14')
#         model = request.GET.get('model14')
#         year = request.GET.get('year14')

#         cursor = connection.cursor()
#         query = f"""
#                 SELECT AVG(Amount) as AvgSellPrice
#                 FROM Car as c
#                 INNER JOIN `Order` as o on c.VIN = o.VIN
#                 WHERE"""

#         params = []

#         if make:
#             query += " Make = %s"
#             params.append(make)
#         if model:
#             if params:
#                 query += " AND"
#             query += " Model = %s"
#             params.append(model)
#         if year:
#             if params:
#                 query += " AND"
#             query += " Year = %s"
#             params.append(year)

#         if not params:
#             query = "SELECT AVG(Amount) as AvgSellPrice FROM Car as c INNER JOIN `Order` as o on c.VIN = o.VIN"

#         cursor.execute(query)
#         avg_sell_price = cursor.fetchall()

#         avg_sell_price_details = [
#             {
#                 'AvgSellPrice': row[0]
#             }
#             for row in avg_sell_price
#         ]

#         context = {
#             'avg_sell_price_details': avg_sell_price_details
#         }
#         return render(request, '14_avg_sell_price.html', context)

#     except OperationalError as e:
#         error_message = str(e)
#         return render(request, 'error.html', {'error_message': error_message})

#     except Exception as e:
#         error_message = "An unexpected error occurred: " + str(e)
#         return render(request, 'error.html', {'error_message': error_message})


# Fix misuse of parameterized queries
def avg_sell_price_sql(request):
    try:
        make = request.GET.get('make14')
        model = request.GET.get('model14')
        year = request.GET.get('year14')

        query = """
                SELECT AVG(Amount) AS AvgSellPrice
                FROM Car AS c
                INNER JOIN `Order` AS o ON c.VIN = o.VIN
                WHERE 1=1"""  # Use WHERE 1=1 for easier query concatenation

        params = []

        if make:
            query += " AND Make = %s"
            params.append(make)
        if model:
            query += " AND Model = %s"
            params.append(model)
        if year:
            query += " AND Year = %s"
            params.append(year)

        cursor = connection.cursor()
        cursor.execute(query, params)  # Pass parameters as a second argument
        avg_sell_price = cursor.fetchall()

        avg_sell_price_details = [{'AvgSellPrice': row[0]} for row in avg_sell_price]

        context = {
            'avg_sell_price_details': avg_sell_price_details
        }
        return render(request, '14_avg_sell_price.html', context)

    except OperationalError as e:
        error_message = str(e)
        return render(request, 'error.html', {'error_message': error_message})

    except Exception as e:
        error_message = "An unexpected error occurred: " + str(e)
        return render(request, 'error.html', {'error_message': error_message})

def delete_user_sql(request):
    try:
        user_id = request.GET.get('userID')

        if user_id:
            cursor = connection.cursor()
            query = """
                DELETE FROM User
                WHERE UserID = %s
            """
            try:
                cursor.execute(query, [user_id])
                success_message = f"User with ID {user_id} has been deleted successfully."
            except Exception as e:
                success_message = f"Error deleting user: {str(e)}"
            finally:
                cursor.close()
        else:
            success_message = "Please provide a valid User ID."

        context = {
            'success_message': success_message
        }

        return render(request, '15_delete_user.html', context)
    except OperationalError as e:
        error_message = str(e)
        return render(request, 'error.html', {'error_message': error_message})

    except Exception as e:
        error_message = "An unexpected error occurred: " + str(e)
        return render(request, 'error.html', {'error_message': error_message})
