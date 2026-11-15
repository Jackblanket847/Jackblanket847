# Filesystem Tree

A mirror of the Linux root filesystem hierarchy (FHS) in this repo.

```
/
├── bin/
├── boot/
├── dev/
├── etc/
├── home/
├── lib/
├── media/
├── mnt/
├── opt/
├── proc/
├── root/
├── run/
├── sbin/
├── srv/
├── sys/
├── tmp/
├── usr/
└── var/
```

Each folder holds a `README.md` describing its FHS purpose. The layout is validated on every push by `.github/workflows/validate-filesystem-tree.yml`.
