exports.getMatch = (req, res) => {
  
    res.status(200).json({
      status: 'success',
      data: {
        match: "This is a match"
      },
    });
  };