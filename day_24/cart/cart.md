```py

from decimal import Decimal

from store.models import Product

class Cart:
    def __init__(self, request):
        # Django'nun oturum objesini self.session'a atar.
        self.session = request.session
        # self.session = request.session: Django'nun oturum 
        # (session) objesini, Cart sınıfının bir örneği 
        # oluşturulduğunda oluşturulan request objesinden 
        # alır ve self.session değişkenine atar. Bu, oturum 
        # üzerindeki değişiklikleri takip etmek için kullanılır.
        
        # Oturumun içinde 'cart' adlı bir anahtar var mı kontrol eder.
        cart = self.session.get('cart')
        # cart = self.session.get('cart'): Oturum içindeki 
        # 'cart' adlı anahtarı alır. Eğer 'cart' anahtarı yoksa, 
        # cart değişkenine None değerini atar.
        
        
        # Eğer 'cart' anahtarı oturumda yoksa, yeni bir 'cart' 
        # sözlüğü oluşturup oturuma ekler.
        if "cart" not in request.session:
            cart = self.session["cart"] = {}
            
        # "cart" not in request.session:: Eğer 'cart' anahtarı 
        # oturumda yoksa, bu koşul bloğuna girer.
        # 3.1. cart = self.session["cart"] = {}: 
        # Yeni bir 'cart' sözlüğü oluşturur ve bu 
        # sözlüğü oturuma ekler. Bu yeni sepet, self.cart 
        # değişkenine atılır.    
            
        
        # self.cart'a, oturumdaki 'cart' sözlüğünü atar.
        self.cart = cart
        
        # self.cart = cart: Eğer 'cart' anahtarı oturumda varsa, 
        # mevcut 'cart' sözlüğünü self.cart değişkenine atar. 
        # Eğer 'cart' anahtarı oturumda yoksa, yeni bir 'cart' 
        # sözlüğü oluşturup oturuma ekledikten sonra bu yeni sepeti 
        # self.cart değişkenine atar.
        
# Cart sınıfını oluşturuyoruz. __init__ metodunda, 
# kullanıcı oturumu üzerinden alışveriş sepetini yönetmek 
# için gerekli işlemleri gerçekleştiriyoruz. Eğer 
# kullanıcının sepeti daha önce oluşturulmamışsa, 
# boş bir sepet oluşturuyoruz.
        
# ------------------------------------------------------
    def add(self, product, product_qty):
        # Ürünün ID'sini bir stringe çevirir.
        product_id = str(product.id)
        
        # Eğer belirtilen ürün ID'si sepet içinde varsa:
        if product_id in self.cart:
            # Sepet içindeki ilgili öğenin 'qty' (miktar) değerini günceller.
            self.cart[product_id]["qty"] = product_qty
        else:
            # Eğer belirtilen ürün ID'si sepet içinde yoksa, 
            # yeni bir öğe (ürün) ekler.
            self.cart[product_id] = {"price": str(product.price), "qty": product_qty}
            # Bu öğenin 'price' (fiyat) değeri ürünün fiyatı, 
            # 'qty' (miktar) değeri ise belirtilen miktar olacaktır.

        # Django session'ın değiştiğini işaretler. 
        # Bu, Django'nun oturumu kaydetmesi gerektiğini anlamasını sağlar.
        
        self.session.modified = True

        # Django session'ın değiştiğini işaretler. 
        # Bu, Django'nun oturumu kaydetmesi gerektiğini 
        # anlamasını sağlar. Bu durumda, sepet üzerinde 
        # yapılan değişikliklerin session'a kaydedilmesi 
        # için bu işlemi yapmak önemlidir.
        
        
#add metodu, sepete ürün eklemek için kullanılır. 
# Eğer ürün sepette varsa, miktarını günceller. 
# Yoksa, yeni bir ürün ekler.
# ------------------------------------------------------


        
# ------------------------------------------------------
    def delete(self, product):
        # Ürün ID'sini bir stringe çevirir.
        product_id = str(product)
        
        # Eğer belirtilen ürün ID'si sepet içinde varsa:
        if product_id in self.cart:
            # Sepet içindeki ilgili öğeyi (ürünü) siler.
            del self.cart[product_id]

        # Django session'ın değiştiğini işaretler. 
        # Bu, Django'nun oturumu kaydetmesi gerektiğini anlamasını sağlar.
        self.session.modified = True
        # Django session'ın değiştiğini işaretler. 
        # Bu, Django'nun oturumu kaydetmesi gerektiğini 
        # anlamasını sağlar. Bu durumda, sepet üzerinde 
        # yapılan değişikliklerin session'a kaydedilmesi 
        # için bu işlemi yapmak önemlidir.
        
# delete metodu, belirli bir ürünü sepette silmek için kullanılır.        
# ------------------------------------------------------
        
# ------------------------------------------------------
    def update(self, product, qty):
        # Ürün ID'sini bir stringe çevirir.
        product_id = str(product)
        
        # Yeni miktar değerini bir değişkene atar.
        product_quantity = qty
        
        # Eğer belirtilen ürün ID'si sepet içinde varsa:
        if product_id in self.cart:
            # Sepet içindeki ilgili öğenin 'qty' (miktar) değerini günceller.
            self.cart[product_id]["qty"] = product_quantity
        
        # Django session'ın değiştiğini işaretler. 
        # Bu, Django'nun oturumu kaydetmesi gerektiğini anlamasını sağlar.
        self.session.modified = True

        
# update metodu, bir ürünün miktarını güncellemek için kullanılır.

# Bu metodun amacı, belirtilen bir ürünün sepet içindeki miktarını 
# güncellemektir. Şu adımları izler:

#     product_id = str(product): Belirtilen ürünün ID'sini 
# bir stringe çevirir. Bu, ürünleri sözlüklerde anahtar 
# olarak kullanmak için bir önlem sağlar.

#     product_quantity = qty: Yeni miktar değerini bir 
# değişkene atar. Bu, güncellenecek olan miktarı temsil eder.

#     if product_id in self.cart:: Belirtilen ürün ID'si, 
# sepet içinde bulunuyorsa, bu bloğa girer.

#     3.1. self.cart[product_id]["qty"] = product_quantity:
# Sepet içindeki ilgili öğenin 'qty' (miktar) değerini günceller.

#     self.session.modified = True: Django session'ın 
# değiştiğini işaretler. Bu, Django'nun oturumu kaydetmesi 
# gerektiğini anlamasını sağlar. Bu durumda, sepet üzerinde 
# yapılan değişikliklerin session'a kaydedilmesi için bu işlemi yapmak önemlidir.

# Bu metod, belirli bir ürünün sepet içindeki miktarını 
# günceller ve bu güncellemenin Django oturumu üzerinde kaydedilmesini sağlar.
# ------------------------------------------------------


# ------------------------------------------------------
    def __len__(self):
        # self.cart.values() ifadesi, sepetteki 
        # her bir öğenin değerini (value) içeren 
        # bir sözlük görünümü oluşturur.
        # Her bir öğenin 'qty' (miktar) anahtarına karşılık gelen değeri alır.
        # Bu değerlerin toplamını sum fonksiyonu ile hesaplar.
        return sum(item['qty'] for item in self.cart.values())

    
# __len__ metodu, sepetteki toplam ürün sayısını döndürür.
# Bu metodun amacı, sepetin içindeki toplam ürün sayısını 
# hesaplamaktır. Şu adımları izler:

#     self.cart.values(): Sepetteki her bir öğenin değerini 
# (value) içeren bir sözlük görünümü oluşturur.
#     item['qty'] for item in self.cart.values(): 
# Bu sözlük görünümündeki her bir öğenin 'qty' (miktar) 
# anahtarına karşılık gelen değeri alır.
#     sum(...): Alınan miktar değerlerinin toplamını hesaplar.
#     return: Bu toplam miktarı döndürür. Bu sayede, 
# bu metodun çağrıldığı yerde sepetin toplam ürün sayısına erişilebilir.

# Bu metodun kullanımı, örneğin, bir alışveriş sepetinde kaç 
# farklı ürün olduğunu veya toplamda kaç adet ürün bulunduğunu 
# belirlemek için kullanılabilir.
# ------------------------------------------------------
    
    def __iter__(self):
        # Sepette bulunan tüm ürünlerin ID'lerini alır.
        all_products_ids = self.cart.keys()

        # Ürün modelinden, sepet içindeki ürünlerin 
        # bilgilerini filtreleyerek çeker.
        products = Product.objects.filter(id__in=all_products_ids)

        # Sepetin kopyasını alır. Altta açıklama var nosu 1
        cart = self.cart.copy()

        # Her bir ürün için, sepet içindeki ilgili 
        # öğeye ürün bilgilerini ekler.
        for product in products:
            cart[str(product.id)]["product"] = product

        # Sepet içindeki her bir öğeyi gezinerek, 
        # Decimal türüne çevirilmiş fiyat ve toplam tutar bilgilerini ekler.
        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total"] = item["price"] * item["qty"]

            # yield ifadesi ile her bir öğeyi döndürür. 
            # Bu sayede bu metodun çağrıldığı yerde for döngüsü ile gezilebilir.
            yield item

            
#__iter__ metodu, sepet içindeki ürünleri gezinmeyi sağlar. 
# Her bir ürünün fiyatını Decimal türüne çevirir ve 
# toplam fiyatı hesaplar.
            
    def get_total(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())        
        
# get_total metodu, sepetin toplam tutarını Decimal türünde döndürür.

# ------------------------------------------------------
# Genel özet: Bu kodlar, bir alışveriş sepetini yönetmek 
# için kullanılır. Sepetin içine ürün eklemek, 
# ürün miktarını güncellemek, ürünü silmek, 
# sepetteki toplam ürün sayısını ve toplam tutarı 
# hesaplamak gibi işlemleri gerçekleştiren bir Cart 
# sınıfını içerir. Sepet, kullanıcının oturumu 
# üzerinden yönetilir ve Django modeli Product 
# ile etkileşimde bulunur.
# ------------------------------------------------------

# ------------------------------------------------------
# 1
# Sepetin kopyasını almanın temel nedeni, orijinal 
# sepetin değiştirilmesini önlemek ve bu değişikliklerin 
# sadece geçici bir kopyada yapılmasını sağlamaktır. 
# İki ana neden vardır:

    # a
    # Değişmezlik (Immutability): Sepetin kopyasını 
    # almak, orijinal sepetin değişmez (immutable)
    # olmasını sağlar. Eğer orijinal sepet üzerinde
    # değişiklik yapılırsa, bu değişiklikler tüm kod
    # boyunca etki eder ve başka yerlerde bu sepet 
    # nesnesi kullanıldığında beklenmeyen sonuçlara
    # yol açabilir. Kopya alarak, sadece kopya  
    # üzerinde değişiklik yapılır ve orijinal 
    # sepetin yapısı korunmuş olur.

    #b
    # Güncellenmiş Verilerin Güvenliği: Django'da,  
    # session verileri genellikle sözlükler gibi 
    # mutable (değiştirilebilir) veri tipleridir. 
    # Bu durumda, orijinal sözlüğü kopyalayarak, 
    # bir değişiklik yapıldığında, orijinal session 
    # verisinin değişmemesini ve güncellenmiş bir kopya 
    # üzerinden işlem yapılmasını sağlar. Ayrıca, 
    # self.cart.copy() ifadesi, orijinal sözlüğün
    # kopyası üzerinde işlem yapılmasını, 
    # orijinal sözlüğü etkilememesini sağlar.

# Bu yaklaşım, programın beklenmeyen yan etkilerle 
# başa çıkmasına yardımcı olur ve kodun daha
# öngörülebilir ve güvenli olmasını sağlar.
# ------------------------------------------------------

```