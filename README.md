# django_project
Rental_management source code

動機:
1.將原本需要人力的工作:如預約看房、租客填寫個人資訊等事情，交由資料庫及其系統做處理，減少因人工操作而產生的疏失。
2.將用戶能得到的資訊列在網站上，如房間內的配置，房間租金等。而租客能看到本期自己已使用的電費度數。將資訊公開。

功能:
一般使用者(非住戶):預約看房
住戶:查看及更改個人資訊、查看本期電費度數
房東:上傳房間圖片、上傳電費資訊、查看看房預約、查看住戶資訊、更改房客身分。

使用技術:
1.註冊:auth使用者驗證寄信到gmail啟用帳戶
2.登入:利用modelForm製作表單，使用者驗證
		Session存入使用者身分，供各網頁判別
3.首頁:用iframe顯示google地圖租屋位置,
     url反解 進入房間詳細資訊
     取得使用者上傳的圖片,
     點擊messenger、google圖案可直接私訊
4.預約看房:modelForm存入資料庫
5.租戶資訊:modelForm表單修改個人資訊
6.個人電費資訊:撈資料顯示
7.上傳房間照片:modelForm上傳圖片
8.電費資訊:透過script 寫function 點擊button把參數傳回更改住戶繳費狀態
9.公布電費:一般的Form，讀取傳回的資料後做運算，再更新資料庫中兩個表Electricity_personal和Electricity_total，完成自動算出各房應繳電費
10.房客列表:透過script 寫function 點擊button把參數傳回已刪除搬離的房客


