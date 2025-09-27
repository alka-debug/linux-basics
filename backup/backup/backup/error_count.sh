#!/bin/bash
grep -c "error" /var/log/*.log | awk -F: '$2 > 0'
