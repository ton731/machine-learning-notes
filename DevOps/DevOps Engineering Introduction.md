# DevOps Engineering Introduction


###### tags: `DevOps/MLOps`


- Course links
    - [DevOps Engineering Course for Beginners](https://www.youtube.com/watch?v=j5Zsa_eOXeY)


### Introduction
- DevOps
    - DEV: plan -> code -> build -> test
    - OPS: release -> deploy -> operate -> monitor
    - DevOps: DEV -> OPS -> DEV -> OPS -> ...
- DevOps Engineering Definition
    - Practical use of DevOps within software engineering teams. Being able to build, test, release and monitor applications.
- **DevOps Engineering Pillars**
    - **Pull Request Automation**
        - 當code有改動而有pull-request/merge-request時，可以去automate: Continous Integration (CI), Per change ephemeral environments, Automated security scanning, Notifications to reviewers。
    - **Deployment Automation**
        - 將新的feature部署到一小部分user當作final test before rolling it out publically。
        - 在沒有造成downtime的情況將新版本啟用。
        - 當新版本有問題時，能roll back回去之前版本。
    - **Application Performance Management**
        - Metrics, Logging, Monitoring, Alerting。


## Code Review Automation

### TDD (Test Driven Development)
- **TDD Definition:** A coding methodology where tests are written before code is written
    - Without TDD: 規劃要做什麼 --> 根據規格寫code --> 用簡單的script測試
    - With TDD: 規劃要做什麼 --> 寫一些當product work時就會通過的test function --> 持續寫code直到所有test都通過
- 包含：Unit tests, Integration tests, System (end to end) tests, 和 Acceptance tests
- TDD目標：當有東西壞掉時，能知道，並且也知道是哪裡壞掉，並最後確保整個系統能正常運作。
- 用TDD和不用TDD寫出來的結果可能都一樣，但TDD強迫你去prioritize task。


### CI (Continuous Integration)
- **CI Definition:** Developer pushing many small changes to a central git repository per day. These changes are verified by an automatic software that runs comprehensive tests to ensure no major issues are seen by customers.
- 3個CI主要好處：
    1. CI is the first step to DevOps automation and helps with code collaboration
    2. CI helps improve developer speed without breaking existing code
    3. CI helps reduce customer churn (顧客流失率) and user satisfication by preventing broken code from publishing
- 許多平台，如Github, GitLab, BigBucket都有提供免費的CI，如Github action。
- **總結：** CI is a vital tool for developer collaboration. Increase collaboration, preven errors, and increase user satisfication.


### Code Coverage
- **Code Coverage:** Methodology that quantitatively measures how comprehensive a code base's tests are. Increasing code coverage often increases stability and reduces bugs.
- 程式碼可分為：
    1. Syntax lines: 如(, ), {, },自己就佔一行的line
    2. Logic lines: 邏輯運算
    3. Branch lines: for, if 
- Code Coverage Formula = total # of non-syntax lines with tests / total num of non-syntax lines
- Branch Coverage Definition: 與其衡量多少行code有備test到，去衡量groups of lines。
- 什麼時候需要考慮code coverage?
    1. 現在產品有users且如果有bug的話users可能就會離開
    2. 現在開發夥伴無法馬上相信，如interns/contractors
    3. 正在work on一個很大的code base，並且有很多testable components
- Common mistake: 當還沒確定一個feature user會不會喜歡時，對這個feature過多的unit test, high coverage會降低開發效率。
- **小結：** If you are working in a large code base using TDD, hiring interns/contractors or have users sensitive to bugs, it's time to measure code coverage.


### Linting
- **Linting Definition:** Linters look at a program's source code and find problems automatically. They are a common feature of pull request automation because they ensure that "obvious" bugs do not make it to production.
- Linter可以用靜態的方式（沒有實際執行code）去尋找code中的bug或是不好的寫法，如不符合命名style的variable、infinite loop等等。這個linter可以也放在CI中，就可以省去reviewer檢查的時間，是一個cheap & convenient的檢查、formatting方式。
- 在CI中，甚至可以用成若linter檢查到不符合style的部分，可以automatically fix這個issue，然後commit成另外一個branch給reviewer檢查。
- **小結：** Any team with more than one developer working in the same codebase should setup a linter to catch abvious bugs.


### Ephemeral Environment
- **Ephemeral Environment Definition:** Ephemeral Environments是指短暫的開發環境。這些環境是根據需要即時創建的，並且當用戶不再需要它們時，很快就被刪除了。Ephemeral Environments可以在持續集成/持續交付（CI/CD）流程中使用，以測試和驗證應用程序的不同版本和分支。它們可以幫助確保每個版本都經過了正確的測試，並且能夠在不同的環境中運行。
- Ephemeral Environment好處：
    - 加速軟體開發lifecycle
    - 讓developers可以向designers, managers, stakeholders分享改變結果
- Continuous Staging Definition: CI/CD is merged with ephemeral environments to form a unified CI/CD and review process for every commit.


## Deployment Strategies

### Virtual Machines (VMs) and Containers
- VM 和 Container 不同：
    - Virtual Machine（虛擬機器）是在一個host主機上運行一個完整的OS，並且在該OS上運行應用程序。它借助虛擬化技術Hypervisor，將一個物理機器模擬成多個虛擬機器，每個虛擬機器都有自己的OS、應用程序和資源（如Memory、Disk、CPU等），需要從host切割出這些資源給VM，且彼此之間相互隔離，且具有良好的安全性。
    - Container（容器）是一種虛擬化技術，它在OS層面上實現，比VM更輕量級、更快速。Container包含了一個應用程序及其所有相依的庫和文件，並且獨立運行在host主機上的操作系統中。不同於VM，container不會從host再切資源出來，多個容器可以共享同一個OS，從而更節省系統資源。此外，容器還具有良好的可移植性和擴展性，能夠快速部署應用程序。
    - more: [淺談虛擬化技術：虛擬機(VM)與容器(Container)之技術價值與比較分析](https://medium.com/mr-efacani-teatime/%E6%B7%BA%E8%AB%87%E8%99%9B%E6%93%AC%E5%8C%96%E6%8A%80%E8%A1%93-%E8%99%9B%E6%93%AC%E6%A9%9F-vm-%E8%88%87%E5%AE%B9%E5%99%A8-container-%E4%B9%8B%E6%8A%80%E8%A1%93%E5%83%B9%E5%80%BC%E8%88%87%E6%AF%94%E8%BC%83%E5%88%86%E6%9E%90-5c10457aad62)


### Deployment Strategies
- **Rolling deployment:**
    - Definitions: 是一種不會造成downtime的deployment方式，藉由逐漸地把整個服務裡面的instances漸漸換成新的instances，直到最後全部都變成新的。
    - 優點：Well supported, No huge bursts (一次只更新一點), Easily reverted (由於是慢慢更新，若遇到問題可以馬上回去)
    - 缺點：Speed 很慢、API Compatability問題（前端可能更新完了但後端還沒，造成有些API call不存在）
    - **小結：** Rolling deployments are relatively simple to understand and generally well supported by orchestrartors. If your users mind when you have downtime, it's an excellent first step to start deploying using a rolling update strategy.
- **Blue/Green deployments:**
    - Definition: 也不會造成downtime的方式。直接start一個完整的新的系統，然後把routing traffic接過去。
    - 優點：Easy to understand, Powerful, Extendable to workflows
    - 缺點：Difficult to make hotfixes, Resource allocation is not convenient, Clusters can affect each other
    - **小結：** Blue/green deployments are a powerful and extensible deployment strategy that works well with teams that are deploying a few times per day. The strategy only starts being problematic in continuous deployment scenarios where there are many services being deployed many times per day.
- **Canary deployments:**
    - Definitions: 是blue/green deployments的一種，但是不會一次對全部的user改成新的，一開始只會對約5%的user使用新的，先確認沒有負面feedback再繼續更新成新的。


### Autoscaling
- **Definitions:** Autoscaling automates horizontal scaling to ensure that the number of workers is porportional to the load on the system.
- Serveless vs. Autoscaling
    - Serverless是一種運行應用程式的方式，它讓開發人員不用擔心基礎架構的管理，只需專注於編寫代碼。在Serverless中，開發人員創建一個函數，然後將其上傳到平台，平台負責運行這個函數。當有請求時，平台會自動啟動一個容器來運行函數，運行完即關閉。Serverless可以大幅簡化開發流程，減少基礎架構成本，提高可擴展性和可靠性。
    - Autoscaling是一種自動調整基礎架構的方式，以應對流量變化和負載增加的情況。在Autoscaling中，系統會根據指標（如CPU使用率、內存使用率、網絡流量等）來監控應用程式的運行情況，當指標超過某個閾值時，系統會自動添加更多的資源來處理負載。反之，當負載減少時，系統會自動減少資源，以節省成本。
    - Use cases: 通常serverless用來跑~100ms的功能，如網頁或是notification service，這些可以很快開始、stateless的，而autosaling跑~1hr的功能，如CI。


### Service Discovery
- 在deployment中一個重要的問題是要讓servies可以互相找到彼此，例如database可能是一個ip，webserver是一個，api又是另外一個。
- 下面幾種情況會讓你需要考慮service discovery：
    1. You wan "zero downtime deployments" or to use other, more complex deployment strategies
    2. You have more than a couple of microservices
    3. You are deploying to several environments (e.g., dev/staging/ephemeral/production) and it's getting unwieldy


## Application Performance Management

### Log Aggregation
- **Definitions:** It's a way of collecting and tagging application logs from many different services into a single dashboard that can easily be searched. 好的log aggregation platform能夠有效的紀錄來自各方的log，並且當有fault出現時能夠很簡單就搜尋的到。
- **ELK (Elastic Search, Logstash, Kibana)**
    - Elastic Search: 儲存資料、資料搜尋檢視，有效地對資料進行儲存和索引
    - Logstash: 資料儲存軟體，可以採集資料、多管道搜集資料並送到指定位置
    - Kibana: 數據分析和可視化平台，可以快速分析大量資料，並以視覺畫圖表和儀表板的方式呈現
- 為什麼使用ELK?
    - ELK功能為智能數據的應用，除了可以處理規模較大的日誌分析，讓資料檢索更有效率外，也能記錄網站訪客流量的訊息。例如：網站資源的訪問者、訪問的裝置、訪問的結果等等。蒐集流量資料提供了許多後續行銷或商機開發的應用，也能幫助網站管理者更加了解網站的使用者。
- 其他log aggregation platform: ELK, Fluentd, DataDog, LogNDA, AWS CloudWatch Logs
- **小結：** log Aggregation is a key tool for diagnosing problems in production. It's relatively simple to install a turnkey solution like ELK or CloudWatch into a production system, and it makes diagnosing and triaging problems in production significantly easier.

### Vital Production Metrics
- If Log Aggregation is the first tool to set up for production monitoring, metrics monitoring should be the second.
- Log aggregation主要是處理文字，因為log本來就是文字。而metric aggregation則是處理數字。
- Prometheus: 一種常見的metric工具，主要包含的功能有：
    - Time series database
    - Retrieval section: 從log的文字抓出數字訊息
    - Alert manager: 當有事件發生時，馬上通知相關人士
    - Web UI: 當有人被通知有識見識，可以透過UI來看哪裡有問題
- 常見的production metrics tools: Promethus / Grafana, Datadog, New Relic, AWS CloudWatch Metrics, Google Cloud Monitoring, Azure Monitor Metrics



