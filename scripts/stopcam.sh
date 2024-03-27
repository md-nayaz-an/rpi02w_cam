#!/bin/bash
kill -9 $(ps aux | grep -i camera | awk 'NR==1 {print $2}')
