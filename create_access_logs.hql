-- Load the access.log file as an external table.
-- "output.format.string" = "%1$s %2$s %3$s %4$s %5$s %6$s %7$s %8$s" 
-- Note that all types must be strings for the regex serde
-- "input.regex" = "^([\\'+\\d.]+) (.{19}) (\\w+) ([\\/+\\w+\\d+\\?+\\=+\\&+\\%+\\.+]+) (\\d+) (\\S+) ([\\w+\\d+\\.+]+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) \\S+ ([\\d.]+) ([\\d.]+).*",

DROP TABLE ACCESS_LOGS3;

CREATE EXTERNAL TABLE ACCESS_LOGS3 (
  ip_address string,
  date_time string,
  method string,  
  uri string,
  status string,
  session_id string,
  api_server string,
  n1 string, 
  n2 string, 
  cid string,
  n3 string,
  pid string,
  sid string,
  pid2 string,
  ms string,
  server string
) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.contrib.serde2.RegexSerDe'
WITH SERDEPROPERTIES
(
"input.regex" = "^([\\'+\\d.\\S+]+) (.{19}) (\\w+) ([\\/+\\S+]+) (\\d+) (\\S+) ([\\w+\\d+\\.+]+) ([\\'+\\d.\\S+\\s+]+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) (\\S+) \\S+ ([\\d.]+) ([\\d.]+).*",
"output.format.string" = "%1$s %2$s %3$s %4$s %5$s %6$s %7$s %8$s %9$s %10$s %11$s %12$s %13$s %14$s %15$s %16$s %17$s"
)
LOCATION '/clouderamovies/a3';
