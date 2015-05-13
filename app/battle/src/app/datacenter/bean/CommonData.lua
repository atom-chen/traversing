--- 公共数据
--
--	包括，玩家信息，银币，金币，战斗力 等等
--
DROP_BREW = 13
local CommonData = class("CommonData")

function CommonData:ctor(item)
    self.GameLoginResponse = {}
    self.LastStminaTime = nil  -- 上次领取体力时间
    self.AccountResponse = {} -- 注册成功返回数据
    self.isTourist = false
    self.totalRecharge = 0
    self.c_BaseTemplate = getTemplateManager():getBaseTemplate()
    self.isHasVipGift = false
    self.netTip = nil
end
-- function CommonData:clear()
--     cclog("---------------CommonData:clear------")
--     self.GameLoginResponse = {}
--     self.LastStminaTime = nil  -- 上次领取体力时间
--     self.AccountResponse = {} -- 注册成功返回数据
--     self.isTourist = false
--     self.signedList = nil
--     cclog("---------------CommonData:clear------")
-- end

function CommonData:setNetTip(tipStr)
    self.netTip = tipStr
end

function CommonData:getNetTip()
    return self.netTip
end

function CommonData:setAccountResponse(data)
    self.AccountResponse = data
end

function CommonData:getAccountResponse()

    return self.AccountResponse
end

--是否是游客登录
function CommonData:setIsTourist(is_tourist)
    self.isTourist = is_tourist
end

function CommonData:getIsTourist()
    return self.isTourist
end

--获取全部数据
function CommonData:getData()
    if self.GameLoginResponse ~= nil then
        return self.GameLoginResponse
    end
    return nil
end

--给全部数据赋值(登录网络协议返回时对通用值进行初始化)
function CommonData:setData(data)

    self.GameLoginResponse = data                       --commonData全部数据

    self.accountId = data.id                            --玩家id
    self.nickname = data.nickname                       --玩家昵称
    self.register_time = data.register_time
    cclog("------新用户的注册时间－－－－－－－"..self.register_time)
    self.vip = data.vip_level                           --vip等级
    self.exp = data.exp                                 --经验
    self.level = data.level                             --等级
    -- self.stamina = data.stamina                         --体力
    self.totalRecharge = data.recharge
    print("登陆数据：data.recharge = ",self.totalRecharge)
    self.newbee_guide_id = data.newbee_guide_id
    print("newbee_guide_id", newbee_guide_id)
    print("---------------------------------------------------")
    -- self.gold = data.gold                               --元宝
    -- self.coin = data.coin                               --金币
    -- self.junior_stone = data.junior_stone               --初级熔炼石
    -- self.middle_stone = data.middle_stone               --中级熔炼石
    -- self.high_stone = data.high_stone                   --高级熔炼石
    -- self.pvp_score = data.pvp_score                     --pvp声望
    -- print("pvp_score", data.pvp_score)

    self.fine_hero = data.fine_hero                     --良将上次免费抽取的时间
    self.excellent_hero = data.excellent_hero           --神兵利器上次抽取时间
    self.fine_equipment = data.fine_equipment           --一般装备上次抽取时间
    self.excellent_equipment = data.excellent_equipment --神兵利器上次抽取时间

    self.pvp_times = data.pvp_times                     --对战次数
    self.pvp_refresh_count = data.pvp_refresh_count     --重置次数
    self.server_time = data.server_time

    self.client_time = os.time()
    print("server_time", self.server_time)
    print("client_time", os.time)

    self.finances = data.finances

    self.login_time = data.server_time

    self.combat_power = data.combat_power
    self.get_stamina_times = data.get_stamina_times     -- 通过邮件获取体力次数
    self.buy_stamina_times = data.buy_stamina_times     -- 购买体力次数
    print("------self.buy_stamina_times--------",self.buy_stamina_times)
    self.last_gain_stamina_time = data.last_gain_stamina_time -- 上次获得体力时间


    self.head = data.head             --头像列表
    self.now_head = data.now_head     --当前头像id

    -- test
    -- self.server_time = os.time({year=2014,month=9,day=20,hour=11,min=6,sec=0})

    -- test data
    -- self:setCoin(10000000)
    -- self:setGold(10000000)
    -- self:setStamina(99)
    -- self:setFineHero( os.time({year=2014,month=9,day=17,hour=10,min=0,sec=0}) )
    -- self:setExcellentHero( os.time({year=2014,month=9,day=17,hour=10,min=0,sec=0}) )
    -- self:setFineEquipment( os.time({year=2014,month=9,day=17,hour=11,min=6,sec=0}) )
    -- self:setExcellentEquipment( os.time({year=2014,month=9,day=17,hour=10,min=9,sec=0}) )
end

-- 新版本玩家资源 data.finances
function CommonData:getFinance(type)
    -- table.print(self.finances)
    -- print("type, value", type, self.finances[type+1])
    if self.finances[type+1] < 0 then
        self.finances[type+1] = 0
    end
    return self.finances[type+1]
end
function CommonData:setFinance(type, num)
    self.finances[type+1] = num
end
function CommonData:subFinance(type, num)
    self.finances[type+1] = self.finances[type+1] - num
end
function CommonData:addFinance(type, num)
    self.finances[type+1] = self.finances[type+1] + num

    getHomeBasicAttrView():updateStamina()
    getHomeBasicAttrView():updateExp()

    getHomeBasicAttrView():updateGold()
    getHomeBasicAttrView():updateCoin()

end

function CommonData:getRegistTime()
    -- cclog("------新用户的注册时间－－－－－－－"..self.register_time)
    return self.register_time
end

-- 装备精华
function CommonData:getEquipSoul()
    return self:getFinance(21)
end

function CommonData:subEquipSoul(num)
    self:subFinance(21, num)
end
function CommonData:addEquipSoul(num)
    self:addFinance(21, num)
end

-- 元气
function CommonData:getYuanqi()
    return self:getFinance(16)
end
-- 元气
function CommonData:setYuanqi(num)
    self:setFinance(16, num)
end
-- 元气
function CommonData:subYuanqi(num)
    self:subFinance(16, num)
end
-- 元气
function CommonData:addYuanqi(num)
    self:addFinance(16, num)
end
--是否有Vip礼包
function CommonData:getVipGift()
   return self.isHasVipGift
    -- body
end
function CommonData:setVipGift(hasVipGift)
    self.isHasVipGift = hasVipGift
    -- body
end

-- 返回模拟的服务器时间（客户端以服务器时间为准）
function CommonData:getTime()
    local nowTime = os.time()
    local diff_time = nowTime - self.client_time
    return self.server_time + diff_time
end
function CommonData:getDay() return os.date("*t",self:getTime()).day end
function CommonData:getMonth() return os.date("*t",self:getTime()).month end
function CommonData:getYear() return os.date("*t",self:getTime()).year end
function CommonData:getCurrHour() return os.date("*t",self:getTime()).hour end
function CommonData:getCurrMin() return os.date("*t",self:getTime()).min end
function CommonData:getCurSec() return os.date("*t", self:getTime()).sec end

--brew
function CommonData:getNectarNum() return self.nectar_num end
function CommonData:setNectarNum(num) self.nectar_num = num end
function CommonData:getNectarCur() return self.nectar_cur end
function CommonData:setNectarCur(num) self.nectar_cur = num end
function CommonData:getBrewTimes() return self.brew_times end
function CommonData:setBrewTimes(times) self.brew_times = times end
function CommonData:getBrewStep() return self.brew_step end
function CommonData:setBrewStep(step) self.brew_step = step end


-- 返回战斗力
function CommonData:getCombatPower() return self.combat_power end
function CommonData:setCombatPower(num) self.combat_power = num end



--------------------------
-- 当前头像ID
    -- if self.now_head == nil then
    --     if self.head == nil then
    --     else
    --         self.now_head = self.head[1]
    --     end
    -- end
-- end
function CommonData:setHead(id) self.now_head = id end

function CommonData:getHead()
    -- if self.now_head == nil then
    --     if self.head == nil then

    --     else
    --         self.now_head = self.head[1]
    --     end
    -- end
    return self.now_head
end

-- 所有头像ID
function CommonData:getHeadList() return self.head end
function CommonData:setHeadLIst(list) self.head = list end

-- 在头像列表中添加头像ID
function CommonData:addHeadLIstId(id) table.insert(self.head, id) end
--------------------------





-- 上次领取体力的时间
function CommonData:getLastStminaTime() return self.LastStminaTime end
function CommonData:setLastStminaTime(time) self.LastStminaTime = time end

-- 补签次数
function CommonData:setRepaireTimes(times) self.repaireTimes = times end
function CommonData:getRepaireTimes() return self.repaireTimes end
-- 签到列表
function CommonData:setSignedList(list)
    self.signedList = list
end
function CommonData:getSignedList() return self.signedList end
--当前签到为哪一组
function CommonData:setSignRound(roundId) self.SignRoundId = roundId end
function CommonData:getSignRound() return self.SignRoundId end
--当前签到为哪一天
function CommonData:setSignCurrDay(currday) self.SignCurrDay = currday end
function CommonData:getSignCurrDay() return self.SignCurrDay end

-- 武魂商店刷新次数
function CommonData:setSoul_shop_refresh_times(times)
     self.GameLoginResponse.soul_shop_refresh_times = self.GameLoginResponse.soul_shop_refresh_times + times
end
function CommonData:getSoul_shop_refresh_times() return self.GameLoginResponse.soul_shop_refresh_times end

-- 查询某天是否签过到
function CommonData:lookIsSigned(day)
    -- cclog("------------setSignedList---111-----"..day)
    -- table.print(self.signedList)
    for k,v in pairs(self.signedList) do
        if v == day then return true end
    end
    return false
end
-- 将某天签到状态改为已签到
function CommonData:setSignedByDay(day)
    -- cclog("-----------setSignedByDay--------")
    table.insert(self.signedList, day)
    -- table.insert(self.signedList, 3)
end
-- 连续签到天数
function CommonData:setContinuousSignDays(days) self.continuousSignDays = days end
function CommonData:getContinuousSignDays() return self.continuousSignDays end
-- 已经获取的连续签到的奖励  保存列表[7，15，25]
function CommonData:setContinuousSignedList(list) self.continuousSignedList = list end
function CommonData:getContinuousSignedList() return self.continuousSignedList end
function CommonData:setContinuousSignedByDay(day) table.insert(self.continuousSignedList, day) end
function CommonData:setCurContinuousSigned(reward) self.curRewardContinuousSigned = reward end
function CommonData:getCurContinuousSigned() return self.curRewardContinuousSigned end
--以获取的额外签到奖励
function CommonData:setExtraSignGiftList(list)
    self.extraSignGiftList = list
end
function CommonData:getExtraSignGiftList()
    return self.extraSignGiftList
end
function CommonData:addExtraSignGiftListByID(id)
    table.insert(self.extraSignGiftList, id)
    cclog("----------------addExtraSignGiftListByID-------")
    table.print(self.extraSignGiftList)
end
-- 在线时间
-- function CommonData:setOnlineTime(time) self.onlineTimes = time end
-- function CommonData:getOnlineTime()
--     if not self.onlineTimes then
--         return 0
--     end
--     local nowTime = os.time()
--     local diff_time = nowTime - self.client_time
--     return self.onlineTimes + diff_time
-- end
function CommonData:setOnlineTime(time)
    -- cclog("---setOnlineTime-----"..time)
    self.onlineTimes = time
    self.getOnlineRec = os.time()
end
function CommonData:getOnlineTime()
    if not self.onlineTimes then
        return 0
    end
    local nowTime = os.time()
    local diff_time = nowTime - self.getOnlineRec
    return self.onlineTimes + diff_time
end

-- function CommonData:getLastOnlineTime() return self.LastOnlineTime end
-- function CommonData:setLastOnlineTime(time) self.LastOnlineTime = time end
-- 在线奖励
function CommonData:setOnlineGiftList(list) self.onlineGiftList = list end
function CommonData:addGotOnlineGift(giftId) table.insert(self.onlineGiftList, giftId) end
-- 查询在线奖励是否领取
function CommonData:isGetOnlineGift(id)
    if self.onlineGiftList == nil then return false end
    for k,v in pairs(self.onlineGiftList) do
        if v == id then return true end
    end
    return false
end
-- 等级奖励
function CommonData:setLevelGiftList(list) self.levelGiftList = list end
-- 添加已获得的等级奖励
function CommonData:addGotLevelGift(giftId) table.insert(self.levelGiftList, giftId) end
-- 查询等级奖励是否已经领取
function CommonData:isGetLevelGift(id)
    if self.levelGiftList == nil then return false end
    for k,v in pairs(self.levelGiftList) do
        if v == id then return true end
    end
    return false
end
-- 连续登陆奖励
function CommonData:setLoginContinueGiftList(list) self.loginContinueGiftList = list end
function CommonData:addLoginContinueGift(giftId) table.insert(self.loginContinueGiftList, giftId) end
function CommonData:isGetLoginContinueGift(id)
    if self.loginContinueGiftList == nil then return false end
    for k,v in pairs(self.loginContinueGiftList) do
        if v == id then return true end
    end
    return false
end
-- 累积登陆奖励
function CommonData:setLoginTotalGiftList(list) self.loginTotalGiftList = list end
function CommonData:addLoginTotalGift(giftId) table.insert(self.loginTotalGiftList, giftId) end
function CommonData:isGetLoginTotalGift(id)
    if self.loginTotalGiftList == nil then return false end
    for k,v in pairs(self.loginTotalGiftList) do
        if v == id then return true end
    end
    return false
end

function CommonData:getLoginTotalGiftList()
    return self.loginTotalGiftList
end

-- 累积登陆时间
function CommonData:setLoginTotalDay(day) self.loginTotalDay = day end
function CommonData:getLoginTotalDay() return self.loginTotalDay end

--连续登录奖励
function CommonData:setLoginContinueDay(day) self.loginContinueDay = day end
function CommonData:getLoginContinueDay() return self.loginContinueDay end

function CommonData:getHeroSoul() return self:getFinance(3) end
-- 增加武魂值
function CommonData:addHero_soul(num)
    --self.GameLoginResponse.hero_soul = self.GameLoginResponse.hero_soul + num
    self:addFinance(3, num)
end

--获取是否能领取累计登陆奖励
function CommonData:getIsCanGetTotleReward()
    -- print("getIsCanGetTotleReward-------")
    local totleBaseList = getTemplateManager():getBaseTemplate():getTotleBaseList()
    -- table.print(totleBaseList)
    -- print("getIsCanGetTotleReward-------")
    -- table.print(self.loginTotalGiftList)
    -- print("11111111111111")


    local loginTotalDay = self:getLoginTotalDay()
    -- print("loginTotalDay=====" .. loginTotalDay)
    for i = 1, loginTotalDay do
        local item = totleBaseList[i]
        local id = item.id
        local isGot = self:isGetLoginTotalGift(id)
        if isGot == false then
            return true
        end
    end
    return false
end

--获取是否可以领取连续登陆奖励
function CommonData:getIsCanGetSeriesReward()
    local serialBaseList = getTemplateManager():getBaseTemplate():getSerialBaseList()
    local serialTotalDay = self:getLoginContinueDay()
    for i = 1, serialTotalDay do
        local item = serialBaseList[i]
        local id = item.id
        local isGot = self:isGetLoginContinueGift(id)
        if isGot == false then
            return true
        end
    end
    return false
end

--获得是否可以领取战队等级奖励
function CommonData:getIsCanGetLevelReward()
    local lvBaglBaseList = getTemplateManager():getBaseTemplate():getLvBag()
    if self.level == 1 then
        return false
    end

    local size = self.level - 1
    for k, v in pairs(lvBaglBaseList) do
        local parameterA = v.parameterA
        if parameterA <= self.level then
            local id = v.id
            local isGot = self:isGetLevelGift(id)
            if isGot == false then
                return true
            end
        end
    end
    return false
end

-- 减少武魂值
function CommonData:reductionHero_soul(num)
    -- self.GameLoginResponse.hero_soul = self.GameLoginResponse.hero_soul - num
    self:subFinance(3, num)
end

-- -- 减少充值币
-- function CommonData:reductionGlod(num)
--     self.GameLoginResponse.gold = self.GameLoginResponse.gold - num
-- end

--pvp声望
function CommonData:getPvpStore()
    return self:getFinance(8)  --self.pvp_score
end
function CommonData:subPvpStore(num)
    -- self.pvp_score = self.pvp_score - num
    return self:subFinance(8, num)
end
function CommonData:setPvpStore(num)
    self:setFinance(8, num)
end
--玩家id
function CommonData:setAccountId(cur_id) self.accountId = cur_id end
function CommonData:getAccountId() return self.accountId end

--玩家头像id
-- function CommonData:setAccountId(cur_id) self.accountId = cur_id end
-- function CommonData:getAccountId() return self.accountId end

--玩家昵称
function CommonData:setUserName(cur_name) self.nickname = cur_name; getHomeBasicAttrView():updateUserName() end
function CommonData:getUserName() return self.nickname end

--vip
function CommonData:setVip(cur_vip)
    self.vip = cur_vip
    getHomeBasicAttrView():updateVip()
end
function CommonData:getVip() return self.vip end

--经验
function CommonData:setExp(cur_exp) self.exp = cur_exp; getHomeBasicAttrView():updateExp()  getNetManager():sendMsgAfterPlayerUpgrade() end
function CommonData:getExp() return self.exp end
function CommonData:addExp(num) self.exp = self:getExp() + num  getHomeBasicAttrView():updateExp()  getNetManager():sendMsgAfterPlayerUpgrade() end

--等级
function CommonData:setLevel(level)

    print("setLevel---------level====", level)
    print("self.level====", self.level)
    self.isLeveled = false
    if self.level < level then
        getNetManager():getInstanceNet():sendGropUpgrade()
        --getNewGManager():setIsGuideLevel()
        self.isLeveled = true

    end
    self.level = level

    --getHomePageView():updateViewLevel()
    getHomeBasicAttrView():updateLevel()
    getHomeBasicAttrView():updateExp()
end

function CommonData:getLevel() return self.level end

--体力
function CommonData:setStamina(cur_stamina)
    self:setFinance(7, cur_stamina)
    getHomeBasicAttrView():updateStamina()
end
function CommonData:getStamina() return self:getFinance(7) end
function CommonData:addStamina(num) self:setFinance(7, self:getFinance(7) + num); getHomeBasicAttrView():updateStamina() end

--购买体力次数
function CommonData:getBuyStaminaTimes() return self.buy_stamina_times end
function CommonData:addBuyStaminaTimes() self.buy_stamina_times = self.buy_stamina_times + 1 end

--元宝
function CommonData:setGold(cur_gold)
    -- self.gold = cur_gold
    self:setFinance(2, cur_gold)
    getHomeBasicAttrView():updateGold()
end
function CommonData:getGold() return self:getFinance(2) end --self.gold end

--金币
function CommonData:setCoin(cur_coin)
    -- self.coin = cur_coin
    if cur_coin <= 0 then
        cur_coin = 0
    end
    self:setFinance(1, cur_coin)
    getHomeBasicAttrView():updateCoin()
end
function CommonData:getCoin() return self:getFinance(1) end -- self.coin end

--一般装备上次抽取时间
function CommonData:setFineEquipment(cur_fine_equipment) self.fine_equipment = cur_fine_equipment end
function CommonData:getFineEquipment() return self.fine_equipment end
--良将上次免费抽取的时间
function CommonData:setFineHero(cur_fine_hero) self.fine_hero = cur_fine_hero end
function CommonData:getFineHero() return self.fine_hero end

--神兵利器上次抽取时间
function CommonData:setExcellentEquipment(cur_excellent_equipment) self.excellent_equipment = cur_excellent_equipment end
function CommonData:getExcellentEquipment() return self.excellent_equipment end
--神将上次免费抽取时间
function CommonData:setExcellentHero(cur_excellent_hero) self.excellent_hero = cur_excellent_hero end
function CommonData:getExcellentHero() return self.excellent_hero end

--初级熔炼石
function CommonData:setJuniorStone(cur_junior_stone) self.junior_stone = cur_junior_stone end
function CommonData:addJuniorStone(num) self.junior_stone = self:addNum(self.junior_stone, num) end
function CommonData:getJuniorStone() return self.junior_stone end

--中级熔炼石
function CommonData:setMiddleStone(cur_middle_stone) self.middle_stone = cur_middle_stone end
function CommonData:addMiddleStone(num) self.middle_stone = self:addNum(self.middle_stone, num) end
function CommonData:getMiddleStone() return self.middle_stone end

--高级熔炼石
function CommonData:setHighStone(cur_high_stone) self.high_stone = cur_high_stone end
function CommonData:addHighStone(num) self.high_stone = self:addNum(self.high_stone, num) end
function CommonData:getHighStone() return self.high_stone end

--对战次数
function CommonData:setPvpTimes(cur_pvp_times) self.pvp_times = cur_pvp_times end
function CommonData:getPvpTimes() return self.pvp_times end

--挑战次数重置的次数
function CommonData:setPvpRefreshCount(cur_count) self.pvp_refresh_count = cur_count end
function CommonData:getPvpRefreshCount() return self.pvp_refresh_count end
function CommonData:updatePvpRefreshCount(count)
    self.pvp_refresh_count = self.pvp_refresh_count + count
end
-- 加num的银子
-- @num: 添加的银子数量
function CommonData:addCoin(num) self:addFinance(1, num);getHomeBasicAttrView():updateCoin(); end
-- 扣除num的银子
-- @num: 银子的数量，正数
function CommonData:subCoin(num) self:subFinance(1, num);getHomeBasicAttrView():updateCoin(); end

-- 加num的金子
-- @num: 添加的金子数量
function CommonData:addGold(num) self:addFinance(2, num);getHomeBasicAttrView():updateGold(); end
-- 扣除num的金子
-- @num: 金子的数量，正数
function CommonData:subGold(num) self:subFinance(2, num); getHomeBasicAttrView():updateGold(); end

-- 修改战斗力
function CommonData:updateCombatPower() getHomeBasicAttrView():updateCombatPower(); end


-----------------------------
------private function-------
-----------------------------

-- 给某值加addNum
function CommonData:addNum(theNum, addNum)
	assert(addNum >= 0, "the add number must more then 0 !")

	theNum = theNum + addNum
	return theNum
end

-- 给某值减去subNum
function CommonData:subNum(theNum, subNum)
	assert(subNum >= 0 and theNum >= subNum, "the sub number must more than 0 !")
	theNum = theNum - subNum
	return theNum
end

function CommonData:countTimer()
    print("～～～～～～～～～～～")
    local recoverTime = getTemplateManager():getBaseTemplate():getStaminaRecoverTime()   -- 300秒
    local max = getTemplateManager():getBaseTemplate():getStaminaMax()                   -- 最大体力
    -- self.during_time = 0
    local x = self.last_gain_stamina_time
    -- self.during_time = self.server_time - x
    self.during_time = self:getTime() - x

    -- print(self.during_time)
    -- self:getTime()

    local function updateTimer(dt)
        -- print("----- updateTimer ------")
        -- self.server_time = self.server_time + 1
        self.during_time = self.during_time + 1
        if self.during_time >= recoverTime then
            -- print("--------- 10到 -------------")
            if self:getFinance(7) < max then
                getNetManager():getActivityNet():sendRecoverStamina()
                self.during_time = 0
                self.last_gain_stamina_time = self:getTime()
            end
        end
    end
    timer.scheduleGlobal(updateTimer, 1.0)
end
function CommonData:countTime()
    return self.during_time
end
-- function CommonData:countOnlineTime()
--     local function updateTimer( dt )
--         self.onlineTimes = self.onlineTimes + 1
--     end
--     if self.timerOnline ~= nil then
--         timer.unscheduleGlobal(self.timerOnline)
--         self.timerOnline = nil
--     end
--     self.timerOnline = timer.scheduleGlobal(updateTimer, 1.0)
-- end

--@return
---- 检测时间是否为可领取体力时间
function CommonData:isFeastTime(_timeCanGet)
    local function getTheTimeMin(_hour, _min)
        return _hour*60 + _min
    end

    local _curHour = self:getCurrHour()
    local _curMin = self:getCurrMin()
    -- print("current :", _curHour,_curMin)
    for k,v in pairs(_timeCanGet) do
        -- print(v.startHour, v.startMin, v.endedHour, v.endedMin)
        if getTheTimeMin(v.startHour,v.startMin) <= getTheTimeMin(_curHour,_curMin) and
                getTheTimeMin(v.endedHour,v.endedMin) > getTheTimeMin(_curHour,_curMin) then
            return true
        end
    end
    return false
end

function CommonData:isEatFeast(_timeCanGet) -- 检测是否已经吃过了
    local _curHour = self:getCurrHour()
    local _curMin = self:getCurrMin()
    local _curDay = self:getDay()
    local _curMonth = self:getMonth()
    local _curYear = self:getYear()
    local _lastTime = self:getLastStminaTime()
    local _lastTimeHour = os.date("*t", _lastTime).hour
    local _lastTimeMin = os.date("*t", _lastTime).min
    local _lastTimeDay = os.date("*t", _lastTime).day
    local _lastTimeMonth = os.date("*t", _lastTime).month
    local _lastTimeYear = os.date("*t", _lastTime).year

    local function getTheTimeMin(_hour, _min)
        return _hour*60 + _min
    end

    local function inWhichTime(hour,min)
        local index = 1
        for k,v in pairs(_timeCanGet) do
            -- print(v.startHour, v.startMin, v.endedHour, v.endedMin)
            if getTheTimeMin(v.startHour,v.startMin) <= getTheTimeMin(hour,min) and
                    getTheTimeMin(v.endedHour,v.endedMin) > getTheTimeMin(hour,min) then
                return index
            end
            index = index + 1
        end
    end

    if _lastTimeYear == _curYear and _lastTimeMonth == _curMonth and _lastTimeDay == _curDay then -- Sameday
        local _curWhich = inWhichTime(_curHour,_curMin)
        local _lastWhich = inWhichTime(_lastTimeHour,_lastTimeMin)
        if _curWhich == _lastWhich then return true -- 同一时间段，已经吃了
        else return false
        end
    else -- not same day
        return false
    end
end

function CommonData:getTimeCanGet()
    local function onToTime(strTime) -- 解析出时间
        local _len = string.len(strTime)
        local _posS, _posE = string.find(strTime, ":")
        if _posS == _posE then
            local _hour = tonumber(string.sub(strTime, 1, _posS-1))
            local _min = tonumber(string.sub(strTime, _posS+1, _len))
            return _hour, _min
        else
            print("!!!base_config表中manual_time有数据错误")
        end
    end

    local _stamina_time = getTemplateManager():getBaseTemplate():getManualTime()

    local _timeCanGet = {}  -- 保存可领取体力的时间{{startHour,startMin,endedHour,endedMin}...}
    for k,v in pairs(_stamina_time) do
        local str = v[1] .. "-" .. v[2]
        _timeCanGet[k] = {}
        _timeCanGet[k].startHour,
        _timeCanGet[k].startMin = onToTime(v[1])
        _timeCanGet[k].endedHour,
        _timeCanGet[k].endedMin = onToTime(v[2])
    end
    return _timeCanGet
end

-- 煮酒
function CommonData:isOpenBrew()
    local startLv = self.baseTemp:getBrewStartLevel()

end

-- pvp
function CommonData:isOpenArena()
    local startLv = self.baseTemp:getArenaLevel()

end

-- 秘境
function CommonData:isOpenRune()
    local startLv = self.baseTemp:getRuneLevel()

end

-- 世界boss
function CommonData:isOpenWorldBoss()
    local startLv = self.baseTemp:openWorldBossLevel()

end
----------------充值活动相关-------------------------
--初始化充值活动
function CommonData:setRechargeActivityData(data)
    cclog("------------初始化充值活动-----------")
    table.print(data)
    self.rechargeData = data
    for k,v in pairs (self.rechargeData) do
        if v.data.recharge_time ~= nil then print("----recharge_time---"..v.data.recharge_time) end
        if v.gift_type == 9 then
            self.rechargeAcc = v.data[1].recharge_accumulation
        end
    end
end
--充值活动是否可领取
function CommonData:rechargeGiftCanGet(id)
    cclog("--------------id---------"..id)
    if self.rechargeData == nil then return false end
    for k,v in pairs(self.rechargeData) do
        if v.gift_id == id then
            return true
        end
    end
    return false
end
--充值活动奖励是否领取过
function CommonData:rechargeGiftIsGot(id)
    if self.rechargeData == nil then return false end
    for k,v in pairs(self.rechargeData) do
        if v.gift_id == id then
            if v.data[1].is_receive == 0 then return false
            elseif v.data[1].is_receive == 1 then return true end
        end
    end
    return false
end
--活动的累计充值数
function  CommonData:getRechargeAcc()
    if self.rechargeAcc == nil then self.rechargeAcc = 0 end
    return self.rechargeAcc
end
--活动在点击领取时候的发送信息
function CommonData:getSendInfo(id)
    for k,v in pairs(self.rechargeData) do
        if v.gift_id == id then
            return v
        end
    end
end
--设置某一奖励领取了
function CommonData:setRechargeGiftGot(id)
    if self.rechargeData == nil then return end
    for k,v in pairs(self.rechargeData) do
        if v.gift_id == id then
            if v.data[1].is_receive == 0 then
            v.data[1].is_receive = 1 end
        end
    end
end
function CommonData:giftCanGetByType(_type)
    for k,v in pairs(self.rechargeData) do
        if v.gift_type == _type then
            if v.data[1].is_receive == 0 then return true end
        end
    end
    return false
end

--解析xxxx-xx-xx xx:xx:xx - yyyy-yy-yy yy:yy:yy的时间类型
function CommonData:analysisTime(timeStr)

    local function toTimeTable(timeStr)

        local timeTab = {}
        local strlen = string.len(timeStr)
        local pos = string.find(timeStr, " ")
        local data = string.sub(timeStr,1,pos-1)
        local timex = string.sub(timeStr,pos+1,strlen)

        local str = data
        local pos = string.find(str,"-")
        local year = tonumber(string.sub(str,1,pos-1))
        str = string.sub(str,pos+1,-1)
        pos = string.find(str,"-")
        local month = tonumber(string.sub(str,1,pos-1))
        local day = tonumber(string.sub(str,pos+1,-1))

        local str2 = timex
        pos = string.find(str2,":")
        local hour = tonumber(string.sub(str2,1,pos-1))
        str2 = string.sub(str2,pos+1,-1)
        pos = string.find(str2,":")
        local min = tonumber(string.sub(str2,1,pos-1))
        local sec = tonumber(string.sub(str2,pos+1,-1))

        timeTab = {year = year,month = month,day = day,hour = hour,min = min,sec = sec}
        return timeTab
    end

    local strlen = string.len(timeStr)
    local startTime = string.sub(timeStr,1,(strlen+1)/2-2)
    local endTime = string.sub(timeStr,(strlen+1)/2+2,strlen)

    local startTimeTab = toTimeTable(startTime)
    local endTimeTab = toTimeTable(endTime)

    return startTimeTab,endTimeTab
end

--充值数据累计
function CommonData:setRechargeNum(rechargeNum)
    self.totalRecharge = rechargeNum
end

--获取充值数据
function CommonData:getRechargeNum()
    return self.totalRecharge
end

return CommonData









