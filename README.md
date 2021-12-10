# Nhận diện tiếng việt trong thực tế

## Nội dung bài toán:
- Cho 1 bức ảnh chỉ ra vùng nào có tiếng Việt và chữ đó là gì?

## Vấn đề gặp phải:
- Các bức ảnh thực tế có nhiều phông chữ và các hình thái khác nhau, vì thế việc sử dụng các model khác như EASYOCR hay TESSERACT OCR không cho kết quả khả quan.

## Cách tiếp cận:
1. Xác định vùng có tiếng việt:
- Xác định bằng CRAFT hoặc EAST
2. Nhận diện vùng tiếng việt đó là chữ gì:
- Training với VietOCR

## Code

1. Clone code và cài thư viện liên quan
```
!git clone https://github.com/thien1892/Recognition_Vietnamese_in_real.git
!cd Recognition_Vietnamese_in_real/
!pip install -r requirements.txt
```

2. Predict kết quả (nếu máy bạn có GPU thay cuda bằng True)
```python
!python test.py \
 --trained_model=<path weights trained CRAFT> \
 --trained_model_vietocr=<path weights trained vietocr> \
 --config_vietocr=<path config vietocr> \
 --test_folder=<path folder img> \
 --cuda False
```
