import React, { useState } from 'react';

const ReviewForm = () => {
  const [reviewText, setReviewText] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);

  const handleAnalyze = async (e) => {
    e.preventDefault();
    setError(null);
    setResult(null);

    if (!reviewText.trim()) {
      setError("Review text tidak boleh kosong.");
      return;
    }

    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8000/api/analyze-review', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ review_text: reviewText }),
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      console.error(err);
      setError("Gagal menghubungi server. Pastikan backend berjalan.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: '0 auto', padding: '20px' }}>
      <h2>Product Review Analyzer</h2>
      <form onSubmit={handleAnalyze}>
        <div style={{ marginBottom: '15px' }}>
          <textarea
            value={reviewText}
            onChange={(e) => setReviewText(e.target.value)}
            placeholder="Masukkan review produk..."
            rows={5}
            style={{ width: '100%', padding: '10px' }}
            disabled={isLoading}
          />
        </div>
        <button 
          type="submit" 
          disabled={isLoading || !reviewText.trim()}
          style={{ 
            padding: '10px 20px', 
            cursor: (isLoading || !reviewText.trim()) ? 'not-allowed' : 'pointer',
            backgroundColor: isLoading ? '#ccc' : '#007bff',
            color: 'white', border: 'none', borderRadius: '4px'
          }}
        >
          {isLoading ? 'Analyzing...' : 'Analyze Review'}
        </button>
      </form>

      {error && (
        <div style={{ marginTop: '20px', padding: '10px', backgroundColor: '#ffebee', color: '#c62828' }}>
          <strong>Error:</strong> {error}
        </div>
      )}

      {result && (
        <div style={{ marginTop: '20px', padding: '15px', border: '1px solid #ddd', backgroundColor: '#f9f9f9' }}>
          <h3>Analysis Result</h3>
          <p><strong>Sentiment:</strong> {result.sentiment_label} ({result.sentiment_score.toFixed(2)})</p>
          <p><strong>Key Points:</strong></p>
          <ul>
            {result.key_points && result.key_points.map((point, i) => <li key={i}>{point}</li>)}
          </ul>
        </div>
      )}
    </div>
  );
};

export default ReviewForm;