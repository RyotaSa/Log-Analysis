# Log-Analysis

**Descroption**

The project will show to build and refine complex queries and use them to draw business conclusions from data.

**Questions**
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Getting Started
**Prerequisite**
- Install Vagrant
- Use Python 3
- Database file(Download or Clone from [full-stack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm), use `newsdata.sql`)

**Instruction**
1. Launch the VM with the command in the full-stack-nanodegree-vm repository:
` vagrant up `
2. Log in with the command:
` vagrant ssh `
3. Go to vagrant directory:
` cd /vagrant `
4. Connect to the installed database and Load the data:
` psql -d news -f newsdata.sql `
5. Since the database has three tables, Check this out:
` \dt `
And
Check table's schema:
` \d <table name> `

## Application Code ##
