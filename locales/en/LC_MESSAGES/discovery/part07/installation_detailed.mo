Þ    !      $              ,     -     H     Y     i     x            U   ®  !     =   &  %   d          £  Î   ¿          ®  %   Ë  I   ñ  ;   ;  J   w  8   Â  ;   û  O   7  4     A   ¼  .   þ     -     ¾  N   Ö  <   %  7   b  1       Ì     [
     t
     
     
     ª
     ¼
     Ñ
  1   æ
          3     N     m     y               %     7  .   K     z  0     &   Ã  )   ê  +     %   @  6   f       _   ½       :   4  !   o  )        »   1. íì í¨í¤ì§ ì¤ì¹ 2. Hadoop ì¤ì¹ 3. MySQL ì¤ì¹ 4. Hive ì¤ì¹ 5. Druid ì¤ì¹ 6. Metatron ì¤ì¹ 7. Preptool ì¤ì¹ File dataset createdë¼ê³  ëì¤ë©´ preptoolì´ ì ëë¡ ëìíë ê²ìëë¤. HDFS ë° Yarnì ì¤íí©ëë¤. Hadoopì´ ì ëë¡ ì¤ì¹ëìëì§ íì¤í¸í´ë´ëë¤. Hive metastoreë¥¼ ì´ê¸°íí©ëë¤. Hiveë¥¼ ììí©ëë¤. Hiveì ì ìí´ë´ëë¤. Linux OSë§ ì ê³µë íê²½(CentOS 7)ì ê¸°ì¤ì¼ë¡, ë°ì´í° íë¦¬í¼ë ì´ì ê¸°ë¥ì ëª¨ë ì¬ì©í´ë³¼ ì ìëë¡ ë©íí¸ë¡ ì ì¤ì¹, ì¤ì íë ê²ì ëí ê°ì´ë ë¬¸ììëë¤. Metatronì ì´ê¸°íí©ëë¤. MySQLì ì ìí´ë´ëë¤. SSH ìë²ë¥¼ ë¤ì ììí©ëë¤. http://localhost:8090/ ì¼ë¡ ì ìì´ ëë¤ë©´ ì±ê³µí ê²ìëë¤. ê³ìí´ì ë£¨í¸ë¡ ë¤ì ëªë ¹ë¤ì ì¤íí©ëë¤. ë¤ì ë´ì©ì /root/.ssh/configì ë¤ì ë´ì©ì ì¶ê°í´ì£¼ì¸ì. ë¤ì íì¼ë¤ì $HADOOP_CONF_DIRì ë£ì´ì£¼ì¸ì. ë¤ì íì¼ë¤ì $METATRON_HOME/confì ë£ì´ì£¼ì¸ì. ë¤ì íì¼ë¤ì ë¤ì´ë¡ë ë°ìì ì§ì ë ìì¹ë¡ ë£ì´ì£¼ì¸ì. ë¤ì íì¼ì $HIVE_HOME/confì ë£ì´ì£¼ì¸ì. ë¤ìì ëªë ¹ì íµí´ ììí¨ì¤ìëë¥¼ ììëëë¤. ë£¨í¸ë¡ ë¤ì ëªë ¹ë¤ì ì¤íí©ëë¤. ë£¨í¸ë¡ ë¤ì ëªë ¹ë¤ì ì¤íí©ëë¤. Hadoop ë°ì´ëë¦¬ë ê°ê¹ì´ mirrorë¥¼ íµí´ì ë¤ì´ë¡ë ë°ë ê²ì´ ë ì¢ìµëë¤. ìì¸ ì¤ì¹ ê°ì´ë ì í¨ì¤ìëë¥¼ ì´ì©í´ì mysql_secure_installationì ì¤íí©ëë¤. ì´ì  http://localhost:8180/ ì¼ë¡ ì ìíë©´ ë©ëë¤. ì§íìí©ì ë³´ë ¤ë©´ log íì¼ì tail íì¸ì. íì¤í¸ì© íì¼ì ë¤ì´ë¡ë ë°ìµëë¤. Project-Id-Version: metatron discovery docs 0.4.2
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2020-02-07 19:03+0900
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: en
Language-Team: en <LL@li.org>
Plural-Forms: nplurals=2; plural=(n != 1)
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.7.0
 1\. Install requirements 2\. Install Hadoop 3\. Install MySQL 4\. Install Hive 5\. Install Druid 6\. Install Metatron 7\. Install Preptool If you get "File dataset created", then it works. Run HDFS and Yarn daemons. Test if Hadoop works fine. Initialize the Hive metastore. Start Hive. Connect to Hive. This document is a guide for installing metatron and using data preparation feature from the scratch Linux OS environment (CentOS 7). Initialize Metatron. Connect to MySQL. Restart SSH server. Check if you connect to http://localhost:8090/ Run followings by root. Append following contents into /root/.ssh/config Put files below into $HADOOP_CONF_DIR. Put files below into $METATRON_HOME/conf. Put files below into each target locations. Put files below into $HIVE_HOME/conf. Get the temporary password with the following command. Run following commands by root. Run below commands by root. You'd better to download the Hadoop binary from the closest mirror. Install Guide Detailed Run mysql_secure_installation with the temporary password. Connect to http://localhost:8180/ To watch the progress, tail the log file. Download a test file. 