# MnuchinPresserAnalysis

Two samples of the stock market were taken on March 17, 2020. One was taken at 11:00am, and another at 1:00pm.
Both samples had identical parameters: 
  1. stock must be trading between $5 and $15 per share
  2. stock must have gained at least 1% from the opening bell
  
Treasury Secretary Steve Mnuchin spoke at a press briefing around 12:00pm. Therefore, the first sample collected represents the market before the press briefing, and the second sample represents the market after the press briefing.

Each sample was written to its own database table. The two tables were queried to identify which of three categories a stock belongs to:
  1. "The weak" -- stocks that gained at least 1% only after the press briefing
  2. "The strong" -- stocks that had already gained at least 1% before the press briefing and maintained this gain after the press briefing
  3. "The strange" -- stocks that gained at least 1% before the press briefing, but did not maintain this gain after the press briefing.
  
usEquitiesImport.py
 - shows the code that built the database tables
 
mnuchinPresser.py
 - shows the code that queried the database tables
