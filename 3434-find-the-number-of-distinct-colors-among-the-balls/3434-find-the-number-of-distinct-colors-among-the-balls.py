from collections import defaultdict

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n=len(queries)
        ans=[0]*n  # Khởi tạo danh sách kết quả, mỗi phần tử là số màu distinct sau mỗi truy vấn.
        mp={}       # Dictionary (bản đồ) lưu trữ màu sắc hiện tại của mỗi 'x'.  {x: color}
        color=defaultdict(int)  # defaultdict để đếm số lượng mỗi màu. {color: count}
        i=0         # Biến đếm, chỉ số cho danh sách 'ans'.
        for x, c in queries:  # Duyệt qua từng truy vấn.
            if x in mp:   # Nếu 'x' đã tồn tại...
                c0=mp[x]  # Lấy màu sắc cũ của 'x'.
                color[c0]-=1 # Giảm số lượng màu cũ đi 1.
                if color[c0]==0:  # Nếu số lượng màu cũ bằng 0...
                    color.pop(c0)  # Xóa màu cũ khỏi bộ đếm.
            mp[x]=c    # Cập nhật/Thêm 'x' với màu mới 'c'.
            color[c]+=1  # Tăng số lượng màu mới lên 1.
            ans[i]=len(color)  # Số lượng màu distinct hiện tại là độ dài của 'color'.
            i+=1        # Tăng chỉ số.
        return ans  # Trả về danh sách kết quả.

            
        