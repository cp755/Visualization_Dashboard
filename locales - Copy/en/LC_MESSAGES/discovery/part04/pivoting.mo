Þ    
      l               ¼      ½     Î   3  _  r         ù   &  ý           Í   9         	    §	    <  #  R     v  ¡     Û   1       ½   %   'Pivoting'ì´ë Excel ê·¸ë¦¬ëì ê°ì 3ì°¨ì ì°¨í¸ìì íííë¤ë©´ ê·¸ë¦¬ëì êµì°¨ê°ì´ ë§ëë° ííë¡ ì¬ë¬ ê° ì¸ì ì§ê² ë  ì ììµëë¤. Metatronììë 2ì°¨ì ë¨ë©´ì¼ë¡ ì°¨í¸ê° ë³´ì¬ì§ê¸° ëë¬¸ì ì´ê³¼ í ê¸°ì¤ì¼ë¡ ë§ë ë°ë¥¼ ìì ì¬ë ¤ì íííê² ë©ëë¤. ê²°êµ­ ìë ê·¸ ë¦¼ì íì ë¶ë¶ê³¼ ê°ì 2ì°¨ì ííì ì°¨í¸ë¡ ëíë©ëë¤. Excelìì ë°ì´í°ë¥¼ ì´/í/êµì°¨ë¥¼ 2ì°¨ì ê°ì¸ ê·¸ë¦¬ëì ííí ë¤ë©´, Metatronì OLAP Data Discovery ëêµ¬ë¡ì, OLAP Cubeë¥¼ íµí´ ë¤ì°¨ììì ë°ì´í°ë¥¼ ì¡°íí©ëë¤. ìëì ì°¨í¸ë Metatronìì 3ì°¨ì íë¸ë¡ ëíë¸ ì´/í/êµì°¨ ê°ì ì¶ ê·¸ë¦¼ ìëë¤. Pivotingì´ë ì£¼ì´ì§ íì´ë¸ì í¹ì  ì»¬ë¼ë¤ì ê¸°ì¤ì¼ë¡ ê·¸ë£¹ííë ê³¼ì ì ìë¯¸íë©°, ì´ë¥¼ íµí´ ë¶ìê°ë ìì² ë°ì´í°ì í¹ì í ì¸¡ë©´ì ê·¸ëí½ ëë ëíë¡ íì¸í  ì ììµëë¤. ì´ë¬í ê³¼ì ìë ìë¯¸ ìë ë°ì´í°ë¥¼ í¬í¨íë ì»¬ë¼ë¤ì ì´/í/êµì°¨ ì ë°ì ë°°ì¹íë ê²ì í¬í¨í©ëë¤. ì´/í/êµì°¨ ì ë°ì ê°ë ì´/í/êµì°¨ ì ë°ì ê°ëì Excelì êµ¬ì¡°ë¥¼ ìê°íë©´ ì½ê² ì´í´í  ì ììµëë¤. ìë ê·¸ë¦¼ê³¼ ê°ì´ ì´/íì ë¸ë¡ì ì ìíë ì­í ì íê³ , êµì°¨ë ë¸ë¡ ìì ë¤ì´ê° ê°ì ì íë ì­í ì í©ëë¤. ì ê·¸ë¦¼ì ë ê°ì ì°¨ìê° ì»¬ë¼ì ì´ì ë°ì ë°°ì¹íê³  íëì ì¸¡ì ê° ì»¬ë¼ì êµì°¨ì ë°ì ë°°ì¹ í ìíë¥¼ ë³´ì¬ì£¼ê³  ììµëë¤. ì°¨í¸ìë ì´ë ê² ì ë°ì ì¬ë ¤ëì ì»¬ë¼ë¤ì ë°ì´í°ê° íìë©ëë¤. ì°¨í¸ ê·¸ë¦¬ê¸°(pivoting) ì°¨í¸ ì íë³ë¡ ì ë°ë³ íì/ê¶ì¥ ì»¬ë¼ ì íì´ ë¤ë¥´ë©°, ì»¬ë¼ë¤ì ì ë°ì ì¬ë ¤ëê¸° ì ì ë¨¼ì  ì°¨í¸ ì íì ì ííë©´ ì ë°ì íìí ì»¬ë¼ ì íì´ ì ìë©ëë¤. Project-Id-Version: metatron discovery docs 0.4.3
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2019-05-12 19:16+0900
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: en
Language-Team: en <LL@li.org>
Plural-Forms: nplurals=2; plural=(n != 1)
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.7.0
 What is pivoting If the values of an Excel grid are displayed in a three-dimensional chart, each crossing value will be represented by a bar. However, Metatron needs to display such a chart two-dimensionally; for this, bars either in the same column or in the same row get stacked at one point while remaining distinctive from one another. The resulting two-dimensional chart is shown in the gray area of the chart below. Whereas Excel shows data in a two-dimensional grid composed of columns, rows and crosses, Metatron is an OLAP data discovery tool capable of multidimensional data representation. In the following Metatron chart, the column, row, and crossing axes form a three-dimensional cube. Pivoting is a process of grouping the given table by specific columns, thereby helping the analyst view particular aspects of the source data in a graphic or tabular chart. This process includes selecting columns that contain meaningful data and placing them on the column/row/cross shelves. Column/row/cross shelves Think of the structure of Excel to understand what column/row/cross shelves work for. As shown below, the crossing of each column and row cross contains a value. In the example shown above, two dimension columns are placed on the column shelf and one measure column is placed on the cross shelf. The chart displays data resulting from the columns placed on the shelves in this way. Draw a chart (pivoting) Mandatory/recommended column types for each shelf vary depending on the chart type. Selecting a chart type before placing columns on a shelf shows the necessary column types for each shelf. 