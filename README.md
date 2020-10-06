# Edit_BIOS_Setting_Interface

## 簡介
H2OUVE是個可透過command的方式修改BIOS設定的工具，<br>
我們利用Python3撰寫一個簡易的介面，<br>
透過H2OUVE去修改BIOS的設定，<br>
省去使用者一一下指令並修改設定檔的麻煩。<br>
<br>
<br>
當多台server需套用同一個BIOS設定時，<br>
只要先針對一台電腦修改所需的BIOS設定，<br>
匯出設定檔後，<br>
即可透過deploy kit執行這個程式，<br>
讓多台server同時匯入設定檔，<br>
不須一台一台作設定。<br>
<br>
(H2OUVE為版權工具，恕不提供)<br>
<br>
<br>


## 介面
![](http://baidu.com) 
上圖為功能選單，主要分成BIOS設定、Boot Order設定、更改BIOS設定三類<br>
<br>
<br>


## 功能介紹

* BIOS設定 :
1.	Show BIOS Setting file List :<br>
列出存於"BIOSsetting"資料夾裡的bios設定檔<br>
![](http://baidu.com)  
<br>
2.	Export Current BIOS Setting :<br>
匯出目前BIOS的設定，使用者必須輸入檔名，<br>
會自動存為XXX_bios.txt檔，<br>
並放在"BIOSsetting"資料夾<br>
![](http://baidu.com) 
<br>
3.	Import BIOS Setting :
列出存於"BIOSsetting"資料夾裡的bios設定檔，<br>
使用者輸入該設定檔的編號，選擇所需設定檔，並匯入BIOS更改設定<br>
![](http://baidu.com) 
<br>
* Boot Order設定
4.	Show Boot Order Setting file List :<br>
列出存於"BIOSsetting"資料夾裡的boot order設定檔<br>
![](http://baidu.com) 
<br>
5.	Show Current Boot Order :<br>
列出目前BIOS Legacy的Boot Order<br>
![](http://baidu.com) 
<br>
6.	Export Current Boot Order Setting :<br>
匯出目前Boot Order的設定檔，使用者必須輸入檔名，<br>
會自動存為XXX_order.txt檔，並放在"BIOSsetting"資料夾<br>
![](http://baidu.com) 
<br>
7.	Import Boot Order Setting :<br>
列出存於”BIOSsetting”資料夾裡的boot order設定檔，<br>
供使用者選擇所需設定檔，並匯入BIOS更改Boot Order設定<br>
![](http://baidu.com) 
<br>
* 更改BIOS設定
8.	Change Boot Type :<br>
列出三種Boot Type供使用者選擇，<br>
程式會自行更改設定檔中的Boot Type，並匯入BIOS<br>
![](http://baidu.com) 
<br>
9.	Change Legacy Boot Order :<br>
列出目前的Boot Order，<br>
並供使用者輸入1~5去更改Boot Order的順序<br>
(1是順位1，2是順位2 … 依此類推)<br>
![](http://baidu.com) 
<br>