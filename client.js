const axios = require('axios');

const BASE_URL = 'http://localhost:3000';

class ResearchAgentClient {
  constructor(baseUrl = BASE_URL) {
    this.baseUrl = baseUrl;
  }

  async createResearch(question) {
    try {
      const response = await axios.post(`${this.baseUrl}/research`, {
        question
      });
      return response.data;
    } catch (error) {
      console.error('Error creating research:', error.response?.data || error.message);
      throw error;
    }
  }

  async getResearchStatus(topicName) {
    try {
      const response = await axios.get(`${this.baseUrl}/research/${topicName}`);
      return response.data;
    } catch (error) {
      console.error('Error getting research status:', error.response?.data || error.message);
      throw error;
    }
  }

  async updateResearch(topicName, updates) {
    try {
      const response = await axios.put(`${this.baseUrl}/research/${topicName}`, {
        updates
      });
      return response.data;
    } catch (error) {
      console.error('Error updating research:', error.response?.data || error.message);
      throw error;
    }
  }

  async createAnswer(topicName, answer) {
    try {
      const response = await axios.post(`${this.baseUrl}/research/${topicName}/answer`, {
        answer
      });
      return response.data;
    } catch (error) {
      console.error('Error creating answer:', error.response?.data || error.message);
      throw error;
    }
  }

  async listAllResearch() {
    try {
      const response = await axios.get(`${this.baseUrl}/research`);
      return response.data;
    } catch (error) {
      console.error('Error listing research:', error.response?.data || error.message);
      throw error;
    }
  }

  async healthCheck() {
    try {
      const response = await axios.get(`${this.baseUrl}/health`);
      return response.data;
    } catch (error) {
      console.error('Error checking health:', error.response?.data || error.message);
      throw error;
    }
  }
}

// Example usage
async function testResearchAgent() {
  const client = new ResearchAgentClient();

  try {
    // Health check
    console.log('🔍 Checking agent health...');
    const health = await client.healthCheck();
    console.log('Health status:', health);

    // Create new research
    console.log('\n📝 Creating new research...');
    const question = "Can Cursor automate the creation of a backend agent like you?";
    const research = await client.createResearch(question);
    console.log('Research created:', research);

    // Get research status
    console.log('\n📊 Getting research status...');
    const status = await client.getResearchStatus(research.topicName);
    console.log('Research status:', status);

    // List all research
    console.log('\n📋 Listing all research...');
    const allResearch = await client.listAllResearch();
    console.log('All research:', allResearch);

  } catch (error) {
    console.error('Test failed:', error.message);
  }
}

// Run test if this file is executed directly
if (require.main === module) {
  testResearchAgent();
}

module.exports = ResearchAgentClient;
