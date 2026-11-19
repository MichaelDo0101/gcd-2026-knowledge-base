# -*- coding: utf-8 -*-
import io, json
p = r'H:\Other computers\My Laptop (Main)\6. Cá nhân\5. Thương hiệu cá nhân\JCI\GCD 2026\_sync-state.json'
st = json.load(io.open(p, encoding='utf-8'))

new_ids = [
    "d268de8a-9045-44ed-84f6-d999f622ede9",
    "0d5228c0-6fd8-4bb0-b65a-319b030d8f0e",
    "7e3f9488-406d-43d1-95b4-90e4389c4a42",
    "72896cde-9077-4637-b37e-4f49ab24743b",
    "71a2aab3-5126-4ab4-a865-f9dd1add34f6",
    "0326bfe4-35ed-4b56-9a2e-b9bb1f126258",
    "9f9c3b15-4dc8-412d-8150-832624f94704",
    "22ac5c88-7937-46cf-a6c7-4f6790a2fa8c",
    "8a206984-b90c-41a8-a4d3-36e4ca0fad47",
    "972b84de-0eb0-4766-ad78-66c3e6076d86",
    "b85cf177-41ef-4357-8de5-7b795d926b0f",
    "f67327c9-4110-4428-9ead-9897f89129ee",
]
new_files = [
    "assets/2026-11-15-jcitl-su-kien-di-san-1.jpg",
    "assets/2026-11-15-jcitl-su-kien-di-san-2.jpg",
    "assets/2026-11-15-jcitl-su-kien-di-san-3.jpg",
    "assets/2026-11-15-jcitl-truong-phan-tich-gian-1740.jpg",
    "assets/2026-11-15-jcitl-truong-anh-phan-tich-gian-1747.jpg",
    "assets/2026-11-16-jcitl-hanh-1125.jpg",
    "assets/2026-11-16-jcitl-truong-file-logo-1357.jpg",
    "assets/2026-11-16-jcitl-truong-dang-ky-gian-1357.jpg",
    "assets/2026-11-16-jcitl-chin-hang-muc-5tr-1746.jpg",
    "assets/2026-11-16-jcitl-hanh-logo-2012.jpg",
    "assets/2026-11-16-jcitl-son-thong-tin-gian-2036.jpg",
    "assets/2026-11-16-jcitl-son-anh-gioi-thieu-2052.jpg",
]

for i in new_ids:
    if i not in st["processedAssets"]:
        st["processedAssets"].append(i)
for f in new_files:
    if f not in st["savedAssetFiles"]:
        st["savedAssetFiles"].append(f)

st["lastSyncAt"] = "2026-11-19T20:55:00+07:00"
st["lastRunResult"] = (
    "đồng bộ 19/11/2026 20:00. COC GCD 2026: KHÔNG có tin mới (baseline 11/11 20:21). "
    "JCITL: tin mới 19/11 09:27-11:15 — PD rà soát master plan (bỏ note không dùng, phần note xin tài trợ giữ trong dự trù; Anh Thư cập nhật kết quả tài trợ + gian hàng, đưa vào danh mục xin tài trợ gửi đơn vị đồng hành); "
    "Đạt gửi lại hạng mục gian hàng + địa điểm check Plan B tối → phương án DUE với NCC KHÔNG cần P2, cần P3, giảm thiểu hạng mục; "
    "Thủy Anh: nay hoàn thiện thư mời + triển khai tuyến bài truyền thông; Public đội thi đã xong (Quỳnh Anh · Văn Đạt); PD có page chương trình 'Global Citizens Day' để đăng nội dung vòng sau; "
    "PD: lan tỏa chương trình bằng cách thay avatar + đăng thư mời; yêu cầu gói triển khai = phương án DUE với NCC + 1 phương án backup (Mai + Đinh Hạnh xem cùng). "
    "ĐÃ TẢI ĐƯỢC 12 ẢNH MỚI (15-16/11) — gồm ảnh sự kiện Global Crafts Festival 2026 (Hoàng Thành Thăng Long, 13-16/11), poster, sân khấu chính, file logo các đơn vị, "
    "ảnh hệ thống LDP (26 gian đang nhận đề xuất / 0 xác nhận, 5.000.000đ/gian, 34 gian dự kiến) và gói GOBRANDING (logo xuyên suốt + website miễn phí hosting 15 ngày). "
    "KB: as48-as59 (59 ảnh), thêm ngày 19/11 vào timeline, sửa ngày mục master plan (17/11), cập nhật DEADLINES + link gobranding.com.vn/website-mien-phi/. node --check PASS."
)
st["groups"]["JCITL-COC Team Global Citizens Day 2026"]["lastMessageAt"] = "2026-11-19T11:15:00+07:00"
st["groups"]["JCITL-COC Team Global Citizens Day 2026"]["lastMessagePreview"] = "Phạm Văn Trường: đưa phương án về gói triển khai — due + backup (Mai + Đinh Hạnh xem cùng)"
st["knownGaps"] = [
    "JCITL: chưa đọc được khoảng 13/11 18:26 → 15/11 17:06 (danh sách ảo bị cắt trong DOM) — cần mở lại chat và cuộn chậm để bù.",
    "5 ảnh chia sẻ trên CDN Zalo (photo-stal-*.zdn.vn / photo-link-talk) không tải được do CORS — chỉ dùng được ảnh đính kèm qua crm.taskai.vn/files/zalocrm-attachments.",
]

io.open(p, 'w', encoding='utf-8').write(json.dumps(st, ensure_ascii=False, indent=2))
print('STATE OK  processedAssets=%d savedAssetFiles=%d' % (len(st['processedAssets']), len(st['savedAssetFiles'])))
