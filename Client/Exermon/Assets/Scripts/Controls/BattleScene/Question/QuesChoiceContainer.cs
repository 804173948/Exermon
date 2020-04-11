﻿using UnityEngine;

using RecordModule.Data;

using UI.Common.Controls.ItemDisplays;

namespace UI.BattleScene.Controls.Question {

    using Question = QuestionModule.Data.Question;

    /// <summary>
    /// 题目选项容器
    /// </summary>
    public class QuesChoiceContainer :
        ContainerDisplay<Question.Choice>, IItemDetailDisplay<Question> {

        /// <summary>
        /// 常量设置
        /// </summary>

        /// <summary>
        /// 外部组件设置
        /// </summary>
        public QuesPictureContainer pictureContaienr; // 图片容器

        /// <summary>
        /// 显示结果
        /// </summary>
        QuestionSetRecord.IQuestionResult _result = null; // 是否显示答案
        public QuestionSetRecord.IQuestionResult result {
            get { return _result; }
            set {
                _result = value;
                setupSelection();
                requestRefresh();
            }
        }

        /// <summary>
        /// 显示答案解析
        /// </summary>
        bool _showAnswer = false;
        public bool showAnswer {
            get { return _showAnswer; }
            set {
                _showAnswer = value;
                requestRefresh();
            }
        }

        #region 数据控制

        /// <summary>
        /// 同步选择
        /// </summary>
        void setupSelection() {
            clearChecks();
            if (result == null) return;
            var selection = result.getSelection();
            foreach (var sel in selection)
                check(items.Find(c => c.order == sel));
        }

        #endregion

        #region 接口实现

        /// <summary>
        /// 题目
        /// </summary>
        Question question;

        /// <summary>
        /// 配置
        /// </summary>
        /// <param name="container"></param>
        public void configure(IContainerDisplay<Question> container) { }

        /// <summary>
        /// 获取物品
        /// </summary>
        /// <returns></returns>
        public Question getItem() { return question; }

        /// <summary>
        /// 设置物品
        /// </summary>
        /// <param name="item">物品</param>
        /// <param name="index"></param>
        /// <param name="refresh"></param>
        public void setItem(Question item, int index = -1, bool refresh = false) {
            question = item;
            setItems(item.shuffleChoices());
            if (item.isMultiple()) maxCheck = 0;
            else maxCheck = 1;
        }

        public void setItem(Question item, bool refresh = false) {
            setItem(item, -1, refresh);
        }

        public void startView(Question item, int index = -1, bool refresh = false) {
            startView();
            setItem(item, index, refresh);
        }

        public void startView(Question item, bool refresh = false) {
            startView();
            setItem(item, refresh);
        }

        #endregion

    }
}