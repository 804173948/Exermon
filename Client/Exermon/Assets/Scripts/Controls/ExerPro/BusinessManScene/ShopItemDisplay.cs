﻿
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;

using Core.Data.Loaders;

using ItemModule.Data;
using ItemModule.Services;

using UI.Common.Controls.ParamDisplays;
using UI.Common.Controls.ItemDisplays;

using ExerPro.EnglishModule.Data;

namespace UI.ExerPro.BusinessManScene.Controls
{

    /// <summary>
    /// 装备背包显示
    /// </summary>
    public class ShopItemDisplay : SelectableItemDisplay<BaseExerProItem>
    {

        /// <summary>
        /// 常量定义
        /// </summary>

        /// <summary>
        /// 外部组件定义
        /// </summary>
        public BaseItemDisplay itemDisplay;

        public StarsDisplay starsDisplay;

        public Image icon, priceTag;
        public Text name, priceText;

        public Texture2D goldTag, ticketTag, boundTicketTag;

        #region 初始化

        /// <summary>
        /// 初始化
        /// </summary>
        protected override void initializeOnce()
        {
            base.initializeOnce();
            initializeDrawFuncs();
        }

        /// <summary>
        /// 初始化绘制函数
        /// </summary>
        protected void initializeDrawFuncs()
        {
            itemDisplay.registerItemType<BaseExerProItem>(drawItem);
        }

        #endregion

        #region 界面控制

        /// <summary>
        /// 绘制基本信息
        /// </summary>
        /// <param name="item">物品</param>
        protected virtual void drawBaseInfo(BaseExerProItem item)
        {
            name.text = item.name;

            // 处理物品星级和图标情况
            if (item != null)
            {
                starsDisplay?.setValue(item.starId);

                icon.gameObject.SetActive(true);
                icon.overrideSprite = item.icon;
            }
        }

        /// <summary>
        /// 绘制物品价格
        /// </summary>
        /// <param name="item">商品</param>
        void drawPrice(BaseExerProItem item)
        {
            var price = item.price;
            if (price.gold > 0)
            {
                priceText.text = price.gold.ToString();
                setPriceTag(goldTag);
            }
            else if (price.boundTicket > 0)
            {
                priceText.text = price.boundTicket.ToString();
                setPriceTag(boundTicketTag);
            }
            else if (price.ticket > 0)
            {
                priceText.text = price.ticket.ToString();
                setPriceTag(ticketTag);
            }
            else
            {
                priceText.text = "";
                setPriceTag(null);
            }
        }

        /// <summary>
        /// 设置物品价格标签
        /// </summary>
        /// <param name="obj"></param>
        void setPriceTag(Texture2D texture)
        {
            if (texture == null)
                priceTag.gameObject.SetActive(false);
            else
            {
                priceTag.gameObject.SetActive(true);
                priceTag.overrideSprite = AssetLoader.generateSprite(texture);
            }
        }

        /// <summary>
        /// 绘制物品
        /// </summary>
        /// <param name="item">物品</param>
        void drawItem(BaseExerProItem item)
        {
            drawBaseInfo(item);
        }

        /// <summary>
        /// 绘制确切物品
        /// </summary>
        /// <param name="shopItem"></param>
        protected override void drawExactlyItem(ItemService.ShopItem<T> shopItem)
        {
            base.drawExactlyItem(shopItem);
            itemDisplay.setItem(shopItem.item());
            drawPrice(shopItem);
        }

        /// <summary>
        /// 清除物品
        /// </summary>
        protected override void drawEmptyItem()
        {
            base.drawEmptyItem();
            name.text = priceText.text = "";
            icon.gameObject.SetActive(false);
            priceTag.gameObject.SetActive(false);
        }

        #endregion
 
    }
}