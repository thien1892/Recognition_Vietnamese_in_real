# Nhận diện tiếng việt trong thực tế

<img src = 'https://i.imgur.com/lBJrLOx.jpg'>


## Nội dung bài toán:
- Cho 1 bức ảnh chỉ ra vùng nào có tiếng Việt và chữ đó là gì?

## Vấn đề gặp phải:
- Các bức ảnh thực tế có nhiều phông chữ và các hình thái khác nhau, vì thế việc sử dụng các model khác như EASYOCR hay TESSERACT OCR không cho kết quả khả quan.

## Cách tiếp cận:
1. Xác định vùng có tiếng việt:
- Xác định bằng CRAFT hoặc EAST
2. Nhận diện vùng tiếng việt đó là chữ gì:
- Training với VietOCR

## Download pretrain

1. weights trained CRAFT:[click](https://drive.google.com/file/d/1Jsp2v5L69BFkkBnb6f3QSifz7Etd9t9g/view?usp=sharing)
2. weights trained vietocr:[click](https://drive.google.com/file/d/1SrlJmj5UeWHUIhc94cu8YmsRuTTFWbb7/view?usp=sharing)
3. config vietocr:[click](https://drive.google.com/file/d/1BAqAcX14TCsc83fOX8jn15_8r-hUs7t8)

## Code

1. Clone code và cài thư viện liên quan
```
!git clone https://github.com/thien1892/Recognition_Vietnamese_in_real.git
```
```
cd Recognition_Vietnamese_in_real/
```
```
!pip install -r requirements.txt
```

2. Predict kết quả (nếu máy bạn có GPU thay cuda bằng True). Kết quả sẽ lưu lại trong thư mục **Recognition_Vietnamese_in_real/result**
```python
!python test.py \
 --trained_model=<path weights trained CRAFT> \
 --trained_model_vietocr=<path weights trained vietocr> \
 --config_vietocr=<path config vietocr> \
 --test_folder=<path folder img> \
 --cuda False
```