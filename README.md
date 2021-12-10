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
