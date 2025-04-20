class ReportGenerator:
    def generate(self, insights, query):
        report = [
            f"=== MARKET REPORT: {query} ===",
            f"Articles Analyzed: {insights['articles_analyzed']}",
            "",
            "SENTIMENT:",
            f"Positive: {insights['sentiment']['positive']}",
            f"Neutral: {insights['sentiment']['neutral']}",
            f"Negative: {insights['sentiment']['negative']}",
            "",
            "COMPANY MENTIONS:"
        ]
        
        for company, count in sorted(insights['companies'].items(), key=lambda x: -x[1]):
            report.append(f"- {company}: {count}")
        
        report.extend([
            "",
            "TRENDS:"
        ])
        
        for trend, count in insights['trends'].items():
            if count > 0:
                report.append(f"- {trend}: {count}")
        
        # Corrected strategic recommendations section
        report.extend([
            "",
            "STRATEGIC RECOMMENDATIONS:",
            self._generate_recommendations(insights)
        ])
        
        return "\n".join(report)

    def _generate_recommendations(self, insights):
        recommendations = []
        
        if insights['top_company']:
            recommendations.append(
                f"* Focus on {insights['top_company']} (most mentioned competitor)"
            )
        
        if insights['top_trend']:
            recommendations.append(
                f"* Monitor '{insights['top_trend']}' (emerging trend in {insights['trends'][insights['top_trend']]} articles)"
            )
        
        if insights['sentiment']['positive'] > insights['sentiment']['negative']:
            recommendations.append("* Market sentiment is generally positive")
        else:
            recommendations.append("* Caution: Negative sentiment detected")
            
        return "\n".join(recommendations) if recommendations else "No clear recommendations"