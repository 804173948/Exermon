﻿using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using UnityEngine.Events;

/// <summary>
/// 物品容器接口
/// </summary>
public interface IItemContainer<T> : IBaseView where T: class {

    /// <summary>
    /// 配置
    /// </summary>
    /// <param name="items">物品集</param>
    void configure(T[] items);
    void configure(List<T> items);

    /// <summary>
    /// 启动视窗
    /// </summary>
    void startView(int index = 0);

    /// <summary>
    /// 设置物品集
    /// </summary>
    /// <param name="items">物品集</param>
    void setItems(T[] items);
    void setItems(List<T> items);

    /// <summary>
    /// 是否包含物品
    /// </summary>
    /// <param name="item">物品</param>
    /// <returns>是否包含</returns>
    bool containsItem(T item);

    /// <summary>
    /// 获取物品集
    /// </summary>
    /// <returns>物品集</returns>
    T[] getItems();
}

/// <summary>
/// 物品容器显示
/// </summary>
public class ItemContainer<T> : GroupView<SelectableItemDisplay<T>>, IItemContainer<T> where T: class {

    /// <summary>
    /// 常量设置
    /// </summary>
    // public ItemInfo<T> detail; // 帮助界面

    /// <summary>
    /// 外部组件设置
    /// </summary>
    public Text countText; // 个数文本

    /// <summary>
    /// 外部变量设置
    /// </summary>
    public int maxCheck = 0; // 最大选中数
    public int defaultCapacity = 0; // 默认容量

    /// <summary>
    /// 回调函数集
    /// </summary>
    public List<UnityAction> onItemsChangedCallbacks = new List<UnityAction>();
    public List<UnityAction> onSelectChangedCallbacks = new List<UnityAction>();
    public List<UnityAction> onCheckChangedCallbacks = new List<UnityAction>();

    /// <summary>
    /// 内部变量声明
    /// </summary>
    protected List<T> items = new List<T>(); // 物品列表

    protected List<int> checkedIndices = new List<int>(); // 已选中索引

    protected int selectedIndex = -1, lastIndex = -1; // 选择的索引, 上次索引

    #region 初始化
    
    /// <summary>
    /// 配置
    /// </summary>
    public override void configure() {
        base.configure();
        configureItemDisplays();
        configureDetail();
    }
    /// <param name="items">物品集</param>
    public void configure(T[] items) {
        configure(); setItems(items);
    }
    public void configure(List<T> items) {
        configure(); setItems(items);
    }

    /// <summary>
    /// 配置物品帮助组件
    /// </summary>
    void configureDetail() {
        var detail = getItemDetail();
        if (detail != null) detail.configure(this);
    }

    /// <summary>
    /// 配置初始的物品显示项
    /// </summary>
    void configureItemDisplays() {
        for (int i = 0; i < itemDisplaysCount(); ++i)
            createSubView(null, i);
    }

    #endregion

    #region 启动/结束控制

    /// <summary>
    /// 启动视窗
    /// </summary>
    public virtual void startView(int index = 0) {
        base.startView();
        select(index);
    }

    #endregion

    #region 回调控制

    /// <summary>
    /// 添加回调函数
    /// </summary>
    /// <param name="cb">回调函数</param>
    /// <param name="type">回调类型（0：物品变更，1：选择变更，2：选中变更）</param>
    public void addCallback(UnityAction cb, int type = 0) {
        if (cb == null) return;
        switch (type) {
            case 0: onItemsChangedCallbacks.Add(cb); break;
            case 1: onSelectChangedCallbacks.Add(cb); break;
            case 2: onCheckChangedCallbacks.Add(cb); break;
        }
    }

    #endregion

    #region 数据控制

    /// <summary>
    /// 数目文本格式
    /// </summary>
    /// <returns></returns>
    protected virtual string countTextFormat() {
        return "当前选中/总数目：{0}/{1}";
    }

    #region 物品控制

    /// <summary>
    /// 获取物品帮助组件
    /// </summary>
    /// <returns>帮助组件</returns>
    protected virtual IItemDetail<T> getItemDetail() {
        return null;
    }

    /// <summary>
    /// 获取容量
    /// </summary>
    /// <returns>容量</returns>
    public virtual int capacity() {
        return defaultCapacity;
    }

    /// <summary>
    /// 获取物品数量
    /// </summary>
    /// <returns>数量</returns>
    public int itemsCount() {
        return items.Count;
    }

    /// <summary>
    /// 物品显示项数量
    /// </summary>
    /// <returns></returns>
    public int itemDisplaysCount() {
        return Math.Max(maxItemDisplaysCount(), subViews.Count);
    }

    /// <summary>
    /// 物品显示项最大数量
    /// </summary>
    /// <returns></returns>
    public int maxItemDisplaysCount() {
        var capacity = this.capacity();
        return capacity > 0 ? capacity : itemsCount();
    }

    /// <summary>
    /// 设置物品集
    /// </summary>
    /// <param name="items">物品集</param>
    public void setItems(T[] items) {
        clearItems();
        this.items = new List<T>(items);
        onItemsChanged();
    }
    public void setItems(List<T> items) {
        setItems(items.ToArray());
    }

    /// <summary>
    /// 是否包含物品
    /// </summary>
    /// <param name="item">物品</param>
    /// <returns>是否包含</returns>
    public bool containsItem(T item) {
        return items.Contains(item);
    }

    /// <summary>
    /// 获取物品对应的物品显示项
    /// </summary>
    /// <param name="item">物品</param>
    /// <returns>物品显示项</returns>
    public SelectableItemDisplay<T> getItemDisplay(T item) {
        return subViews.Find((item_) => item_.getItem() == item);
    }

    /// <summary>
    /// 增加物品
    /// </summary>
    /// <param name="item">物品</param>
    public void addItem(T item) {
        items.Add(item);
        onItemsChanged();
    }

    /// <summary>
    /// 移除物品
    /// </summary>
    /// <param name="item">物品</param>
    public void removeItem(T item) {
        items.Remove(item);
        onItemsChanged();
    }

    /// <summary>
    /// 转移物品
    /// </summary>
    /// <param name="container">容器</param>
    /// <param name="item">物品</param>
    public void transferItem(ItemContainer<T> container, T item) {
        if (!containsItem(item)) return;
        container.acceptTransfer(prepareTransfer(item));
    }
    public void transferItem<T1>(ISlotItemDisplay<T1, T> slotItem, T item) where T1 : class {
        if (!containsItem(item)) return;
        slotItem.setEquip(prepareTransfer(item));
    }

    /// <summary>
    /// 准备转移
    /// </summary>
    /// <param name="item">物品</param>
    protected virtual T prepareTransfer(T item) {
        removeItem(item);
        return item;
    }

    /// <summary>
    /// 接受转移
    /// </summary>
    /// <param name="item">物品</param>
    protected virtual void acceptTransfer(T item) {
        addItem(item);
    }

    /// <summary>
    /// 清空物品
    /// </summary>
    public void clearItems() {
        items.Clear();
        deselect(); clearChecks();
        requestRefresh();
    }

    /// <summary>
    /// 获取物品集
    /// </summary>
    /// <returns>物品集</returns>
    public T[] getItems() {
        return items.ToArray();
    }

    /// <summary>
    /// 获取物品显示项数组
    /// </summary>
    /// <returns>物品显示项数组</returns>
    public SelectableItemDisplay<T>[] getItemDisplays() {
        return subViews.ToArray();
    }

    /// <summary>
    /// 物品变更回调
    /// </summary>
    protected virtual void onItemsChanged() {
        refreshItemDisplays();
        processForceCheckItems();
        requestRefresh();
        callbackItemsChange();
    }

    /// <summary>
    /// 处理物品改变回调
    /// </summary>
    void callbackItemsChange() {
        foreach (var cb in onItemsChangedCallbacks) cb?.Invoke();
    }

    #endregion

    /// <summary>
    /// 获取循环索引
    /// </summary>
    /// <param name="i">索引</param>
    /// <returns>循环索引</returns>
    protected int getLoopedIndex(int i) {
        var cnt = itemDisplaysCount();
        if (cnt == 0) return -1;
        return (i % cnt + cnt) % cnt;
    }

    /// <summary>
    /// 获取限制索引
    /// </summary>
    /// <param name="i">索引</param>
    /// <returns>限制索引</returns>
    protected int getClampedIndex(int i) {
        var cnt = itemDisplaysCount();
        return Mathf.Clamp(i, 0, cnt-1);
    }

    #region 选择控制

    /// <summary>
    /// 获取选择索引
    /// </summary>
    /// <returns>选择索引</returns>
    public int getSelectedIndex() {
        return selectedIndex;
    }

    /// <summary>
    /// 获取选择项
    /// </summary>
    /// <returns>选择项</returns>
    public SelectableItemDisplay<T> selectedItemDisplay() {
        if (selectedIndex == -1) return null;
        return subViews[selectedIndex];
    }

    /// <summary>
    /// 获取选择物品
    /// </summary>
    /// <returns>物品</returns>
    public T selectedItem() {
        if (selectedIndex == -1) return null;
        return selectedItemDisplay().getItem();
    }

    /// <summary>
    /// 选择
    /// </summary>
    /// <param name="index">索引</param>
    public virtual void select(int index) {
        //Debug.Log("select: " + index);

        index = getLoopedIndex(index);
        if (index >= 0) {
            var item = subViews[index];
            if (!item.isSelectable()) return;
        }

        lastIndex = selectedIndex = index;
        onSelectChanged();
    }

    /// <summary>
    /// 取消选择
    /// </summary>
    public virtual void deselect() {
        //if (selectedIndex < 0) return;
        
        selectedIndex = -1;
        onSelectChanged();
    }

    /// <summary>
    /// 选择上次
    /// </summary>
    public virtual void selectLast(int default_ = 0) {
        if (lastIndex >= 0) select(lastIndex);
        else if (default_ >= 0) select(default_);
        else deselect();
    }

    /// <summary>
    /// 选择改变事件回调
    /// </summary>
    protected virtual void onSelectChanged() {
        requestRefresh();
        updateItemHelp();
        callbackSelectChange();
    }

    /// <summary>
    /// 处理选择改变回调
    /// </summary>
    void callbackSelectChange() {
        foreach (var cb in onSelectChangedCallbacks) cb?.Invoke();
    }

    #endregion

    #region 选中控制

    /// <summary>
    /// 处理强制选中项
    /// </summary>
    void processForceCheckItems() {
        for (int i = 0; i < itemDisplaysCount(); i++)
            if (subViews[i].isForceChecked()) check(i);
    }

    /// <summary>
    /// 最大选中数量
    /// </summary>
    /// <returns>最大选中数量</returns>
    public virtual int maxCheckCount() {
        return maxCheck;
    }

    /// <summary>
    /// 获取选中索引数组
    /// </summary>
    /// <returns>选中索引数组</returns>
    public int[] getCheckedIndices() {
        return checkedIndices.ToArray();
    }

    /// <summary>
    /// 是否选中某项
    /// </summary>
    /// <param name="index">索引</param>
    /// <returns>是否选中</returns>
    public bool isChecked(int index) {
        return checkedIndices.Contains(index);
    }

    /// <summary>
    /// 获取选中项
    /// </summary>
    /// <returns>选中项数组</returns>
    public SelectableItemDisplay<T>[] getCheckedItemDisplays() {
        var cnt = checkedIndices.Count;
        var items = new SelectableItemDisplay<T>[cnt];
        for (int i = 0; i < cnt; ++i) {
            var index = checkedIndices[i];
            items[i] = subViews[index];
        }
        return items;
    }

    /// <summary>
    /// 获取选中物品数组
    /// </summary>
    /// <returns>选中项数组</returns>
    public T[] getCheckedItems() {
        var cnt = checkedIndices.Count;
        var items = new T[cnt];
        for (int i = 0; i < cnt; ++i) {
            var index = checkedIndices[i];
            items[i] = this.items[index];
        }
        return items;
    }

    /// <summary>
    /// 选中
    /// </summary>
    /// <param name="index">索引</param>
    public virtual void check(int index) {
        //Debug.Log("check: " + index);

        index = getLoopedIndex(index);

        var item = subViews[index];
        if (!item.isCheckable()) return;
        if (isChecked(index)) return;

        var cnt = checkedIndices.Count;
        //Debug.Log("cnt: " + cnt + ", max: " + maxCheckCount());
        if (maxCheckCount() > 0 && cnt >= maxCheckCount())
            if (!removeFirstCheckIndex())
                return; // 如果不能移除，则不继续执行
        checkedIndices.Add(index);
        onCheckChanged();
    }

    /// <summary>
    /// 取消第一个选中项
    /// </summary>
    /// <returns>能否执行操作</returns>
    bool removeFirstCheckIndex() {
        for (int i = 0; i < checkedIndices.Count; ++i) {
            var index = checkedIndices[i];
            if (subViews[index].isUncheckable()) {
                checkedIndices.RemoveAt(i);
                return true;
            }
        }
        return false;
    }

    /// <summary>
    /// 取消选中
    /// </summary>
    /// <param name="index">索引</param>
    public virtual void uncheck(int index) {
        //Debug.Log("uncheck: " + index);

        index = getLoopedIndex(index);

        var item = subViews[index];
        if (!item.isUncheckable()) return;
        if (!isChecked(index)) return;

        checkedIndices.Remove(index);
        onCheckChanged();
    }

    /// <summary>
    /// 反转选中
    /// </summary>
    /// <param name="index">索引</param>
    public void toggle(int index) {
        //Debug.Log("toggle: " + index);
        //Debug.Log("Checked: " + string.Join(",", checkedIndices));

        index = getLoopedIndex(index);
        if (isChecked(index)) uncheck(index);
        else check(index);
    }

    /// <summary>
    /// 清空选中
    /// </summary>
    public void clearChecks() {
        checkedIndices.Clear();
        onCheckChanged();
    }

    /// <summary>
    /// 选中改变事件回调
    /// </summary>
    protected virtual void onCheckChanged() {
        requestRefresh();
        callbackCheckChange();
    }

    /// <summary>
    /// 处理物品改变回调
    /// </summary>
    void callbackCheckChange() {
        foreach (var cb in onCheckChangedCallbacks) cb?.Invoke();
    }

    #endregion

    #endregion

    #region 界面控制

    /// <summary>
    /// 绘制数目
    /// </summary>
    void drawCount() {
        if (countText == null) return;
        countText.text = string.Format(countTextFormat(),
            selectedIndex + 1, itemsCount());
    }

    /// <summary>
    /// 绘制数目
    /// </summary>
    void clearCount() {
        countText.text = "";
    }

    #region 物品显示项绘制

    /// <summary>
    /// 创建物品显示组件
    /// </summary>
    void refreshItemDisplays() {
        for (int i=0;i< maxItemDisplaysCount(); ++i) {
            T item = (i < itemsCount() ? items[i] : null);
            createSubView(item, i);
        }
        for(int i= itemDisplaysCount()-1;i>= maxItemDisplaysCount();--i)
            destroySubView(i);
    }

    /// <summary>
    /// 创建物品显示组件
    /// </summary>
    /// <param name="item">物品</param>
    void createSubView(T item, int index) {
        createSubView(index).startView(item);
    }

    /// <summary>
    /// ItemDisplay 创建回调
    /// </summary>
    /// <param name="item">ItemDisplay</param>
    protected override void onSubViewCreated(SelectableItemDisplay<T> sub, int index) {
        sub.configure(this, index);
        base.onSubViewCreated(sub, index);
    }

    #endregion

    #region 物品帮助绘制

    /// <summary>
    /// 绘制物品帮助
    /// </summary>
    public void updateItemHelp() {
        var item = selectedItem();
        if (item == null) drawEmptyHelp();
        else drawExactlyItemHelp(item);
    }

    /// <summary>
    /// 绘制空的帮助
    /// </summary>
    protected virtual void drawEmptyHelp() {
        var detail = getItemDetail();
        if (detail != null) detail.startView(null);
    }

    /// <summary>
    /// 绘制实际物品帮助
    /// </summary>
    /// <param name="item">物品</param>
    protected virtual void drawExactlyItemHelp(T item) {
        var detail = getItemDetail();
        if (detail != null) detail.startView(item, selectedIndex);
    }

    /// <summary>
    /// 清除物品帮助
    /// </summary>
    protected virtual void clearItemHelp() {
        var detail = getItemDetail();
        if (detail != null) detail.requestClear();
    }

    #endregion

    /// <summary>
    /// 刷新视窗
    /// </summary>
    protected override void refresh() {
        base.refresh();
        drawCount();
    }

    /// <summary>
    /// 清除描述
    /// </summary>
    protected override void clear() {
        base.clear();
        clearCount();
        clearItems();
        clearItemHelp();
    }

    #endregion

}
