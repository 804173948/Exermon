﻿using System;
using UnityEngine;
using UnityEngine.UI;

using Core.Data.Loaders;

using GameModule.Services;

using ItemModule.Data;
using PlayerModule.Data;
using QuestionModule.Data;
using BattleModule.Data;

using UI.BattleScene.Controls.ItemDisplays;

/// <summary>
/// 对战匹配场景控件
/// </summary>
namespace UI.BattleScene.Controls.Animators {

    /// <summary>
    /// 玩家准备动作
    /// </summary>
    public class BattlerPrepareAction : BattlerQuestedStatus {

        /// <summary>
        /// 外部组件设置
        /// </summary>
        public UsingItemDisplay itemDisplay;

        #region 初始化

        /// <summary>
        /// 初始化
        /// </summary>
        protected override void initializeOnce() {
            base.initializeOnce();
            selfWindow.addChangeEvent(
                selfWindow.shownState, onShown);
        }

        #endregion

        #region 界面绘制

        /// <summary>
        /// 绘制具体物品
        /// </summary>
        /// <param name="battler">对战玩家</param>
        protected override void drawExactlyItem(RuntimeBattlePlayer battler) {
            base.drawExactlyItem(battler);
            itemDisplay.setItem(battler.roundItem());
        }

        /// <summary>
        /// 清空物品
        /// </summary>
        protected override void clearItem() {
            base.clearItem();
            itemDisplay.requestClear(true);
        }

        #endregion

        #region 动画事件

        /// <summary>
        /// 物品使用效果
        /// </summary>
        public void onItemUse() {
            var item = this.item.roundItem();
            IEffectsConvertable effectItem = null;

            switch ((BaseItem.Type)item.type) {
                case BaseItem.Type.HumanItem:
                    effectItem = (HumanItem)item; break;
                case BaseItem.Type.QuesSugar:
                    effectItem = (QuesSugar)item; break;
                default: return;
            }

            CalcService.ItemEffectProcessor.
                process(this.item, effectItem);

            requestRefresh(true);
        }

        /// <summary>
        /// 完全显示
        /// </summary>
        public void onShown() {
            selfWindow.terminateWindow();
        }

        #endregion
    }
}
