Þ    '      T                               D        ä     é  
   î  &   ù  -      4  N       {     8        =  M   @  `     )   ï       W        u     {       	                   ©     ±     ¹     Ç     Ï     Õ     Ü     å     î  ¨   þ     §  )   µ     ß    ~     
     
     
  =   
     ]
     b
  
   g
     r
     
  Ó   ¢
     v  A   {  $   ½     â  *   å  /        @     L  I   P                ¦  	   ³     ½     Å     Î     Ö     Þ     ì     ô     ú          
          #     ¨  $   µ  _   Ú   DistCp Done Druid Druid ìì§ì ë°ì´í° ì¦ë¶ì ì¬íê¸° ìí´ ì¬ì©í©ëë¤. EXEC HDFS HIVE Query Hadoop File ê´ë¦¬ì ì¬ì©í©ëë¤. Hive ì¿¼ë¦¬ë¥¼ ì¤íí  ë ì¬ì©í©ëë¤. Integratorì ì¡ì ë¸ëë¤(action nodes)ì ìì² ë°ì´í°ë¥¼ Hadoop í´ë¬ì¤í°ìì ìì§Â·ê°ê³µÂ·ì ì¬íê¸° ìí ê°ê°ì ì°ì°ì²ë¦¬ ììì ì ìí©ëë¤. ìëì ê°ì´ ì¬ë¬ ê°ì§ Hadoop ììê³¼ ëªëª ì¶ê°ì ì¸ ê°ë³ ìì¤í ìì(Java, Shell ë±)ì ì§ìí©ëë¤. Java Java Taskë Java Classë¥¼ ì¤ííê³ ì í  ë ì¬ì©í©ëë¤. (ë¨, main í¨ìê° êµ¬íëì´ ìì´ì¼ í©ëë¤.) Localì ìë jarë¥¼ ì¤ííë ë° ì¬ì©í©ëë¤. MR Python, shell ë± ë¡ì»¬ì ìë íì¼ì ì¤ííëë° ì¬ì©í©ëë¤. RDB ìì ë°ì´í°ë¥¼ ê°ì ¸ì¤ê±°ë ê°ë¨í ì¿¼ë¦¬ë¥¼ ì¤íí  ì ìë task ìëë¤. SPARKë¥¼ ì¤ííëë° ì¬ì©í©ëë¤. SSH Source Hadoop Cluster ìì Target Hadoop Clusterì íì¼ ë³µì¬ì ì¬ì©í©ëë¤. Spark Sqoop Sub-Workflow `DistCp`_ `Done`_ `Druid`_ `EXEC`_ `HDFS`_ `HIVE Query`_ `Java`_ `MR`_ `SSH`_ `Spark`_ `Sqoop`_ `Sub-Workflow`_ ê¸°ì¡´ ë§ë¤ì´ì§ Workflowì ì°ê³ ì ì¬ì©ë©ëë¤. ì¬ë¬ê°ì Workflow ë¥¼ ë¬¶ì´ì ì¤ííê³ ì í  ë ê°ê°ì Workflow ë¥¼ Task ë¡ ì ìí©ëë¤. ì¡ì ë¸ë ìë£ì Done íì¼ì ìì±í©ëë¤. ìê²©ì§(remote)ì ìë ëªë ¹ì´ë¥¼ ì¤íí  ë ì¬ì©í©ëë¤. ë¤ë§, remote ìë²ë SSH password-less login ì¤ì ì´ ëì´ ìì´ì¼ í©ëë¤. Project-Id-Version: metatron discovery docs 0.4.3
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2019-05-29 12:55+0900
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: en
Language-Team: en <LL@li.org>
Plural-Forms: nplurals=2; plural=(n != 1)
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.3.4
 DistCp Done Druid Used for incremental ingestion of data into the Druid engine. EXEC HDFS HIVE Query Used to manage Hadoop files. Runs a HIVE query. Action nodes in Integrator define tasks involved in collecting, processing, and ingesting raw data in the Hadoop cluster. The supported Hadoop jobs and individual system tasks (Java, Shell, etc.) are as follows: Java Runs a Java class. (Note that the main function must be defined.) Runs JAR files in a local directory. MR Runs local files such as Python and shell. Retrieves data from RDP or runs a simple query. Runs SPARK. SSH Copies files from the source Hadoop cluster to the target Hadoop cluster. Spark Sqoop Sub-Workflow `DistCp`_ `Done`_ `Druid`_ `EXEC`_ `HDFS`_ `HIVE Query`_ `Java`_ `MR`_ `SSH`_ `Spark`_ `Sqoop`_ `Sub-Workflow`_ Used for association with existing workflows. When running an association of multiple workflows, it defines each workflow as a task. Action nodes Creates a Done file upon completion. Runs a command remotely. Note that SSH passwordless login must be set up for the remote server. 