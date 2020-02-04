﻿using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Events;

using LitJson;

/// <summary>
/// 补全信息窗口
/// </summary>
public class InfoWindow : BaseWindow {

    /// <summary>
    /// 文本常量定义
    /// </summary>
    const string CreateSuccessText = "人物创建完成，点击确认进入游戏！";

    /// <summary>
    /// 外部组件设置
    /// </summary>
    public DateTimeField birthInput; // 名称
    public TextInputField schoolInput, cityInput, 
        contactInput, descriptionInput; // 名称
    
    /// <summary>
    /// 场景组件引用
    /// </summary>
    StartScene scene;

    /// <summary>
    /// 外部系统引用
    /// </summary>
    GameSystem gameSys = null;
    PlayerService playerSer = null;

    #region 初始化

    /// <summary>
    /// 初次初始化
    /// </summary>
    protected override void initializeOnce() {
        base.initializeOnce();
        if (gameSys == null) gameSys = GameSystem.get();
        if (playerSer == null) playerSer = PlayerService.get();
        scene = (StartScene)SceneUtils.getSceneObject("Scene");
    }

    #endregion

    #region 流程控制

    /// <summary>
    /// 创建角色
    /// </summary>
    public void create() {
        doCreate();
    }

    /// <summary>
    /// 执行创建
    /// </summary>
    void doCreate() {
        var birth = birthInput.getValue();
        var school = schoolInput.getText();
        var city = cityInput.getText();
        var contact = contactInput.getText();
        var description = descriptionInput.getText();

        playerSer.createInfo(birth, school, city,
            contact, description, onCreateSuccess);
    }

    /// <summary>
    /// 创建人物成功回调
    /// </summary>
    void onCreateSuccess() {
        var req = gameSys.requestAlert(CreateSuccessText);
        req.addButton(AlertWindow.OKText, scene.refresh);
    }

    #endregion
}
